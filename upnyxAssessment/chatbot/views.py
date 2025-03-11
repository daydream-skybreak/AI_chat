from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import UserSerializer, ChatSerializer
from .models import User
from django.contrib.auth.hashers import check_password


# Create your views here.
@api_view(['POST'])
def sign_up(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        request.session['user_id'] = user.id
        print(user.id)
        return JsonResponse({'message':"User created successfully", 'user': user.username}, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def login(request):
    user = User.objects.filter(username=request.data['username']).first()
    if user and check_password(request.data['password'], user.password):
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            "message": "User signed in successfully",
            'access': str(refresh.access_token),
        }, status=200)
    return JsonResponse({"message":"Invalid credentials"}, status=401)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def token_balance(request):
    user = get_object_or_404(User, id=request.user.id)
    return JsonResponse({"balance": user.tokens}, status=200)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    user = get_object_or_404(User, id=request.user.id)
    if user.tokens < 100:
        return JsonResponse({"message":"Insufficient tokens"}, status=403)
    if "message" not in request.data.keys():
        return JsonResponse({"message":"Message cannot be empty"}, status=400)

    return_message = "this is where the api response will go" # replace this message with an actual response from the ai chat that is going to be integrated
    data = {"user": user.id, "message": request.data['message'], "response": return_message  }
    chat = ChatSerializer(data=data)
    if chat.is_valid():
        chat.save()
        user.tokens -= 100
        user.save()
        return JsonResponse({'message': "Chat have been successfully recorded", "response": chat.data['response']}, status=200)
    return JsonResponse(chat.errors, status=400)

@api_view(['POST'])
def transfer_tokens(request):
    user = get_object_or_404(User, id=request.user.id    )
    recipient = get_object_or_404(User, username=request.data['recipient'])

    if recipient == user:
        return JsonResponse({"message": "Cannot transfer tokens to yourself"}, status=400)

    if user.token_balance <= request.data['amount'] or user.token_balance == 0:
        return JsonResponse({"message": "Insufficient tokens"}, status=403)
    user.token_balance -= request.data['amount']
    recipient.token_balance += request.data['amount']
    user.save()
    recipient.save()

    return JsonResponse({"message": "Tokens transferred successfully"}, status=200)

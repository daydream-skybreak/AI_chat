from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', sign_up, name='signup'),
    path('tokenbalance/', token_balance, name='get_token'),
    path('chat/', chat, name='chat'),
    path('tokentransfer/', transfer_tokens, name='token_transfer'),
    path('logout/', log_out, name='logout')
]


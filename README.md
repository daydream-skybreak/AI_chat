# AI_chat

AI_chat is a Django-based chatbot application that provides a RESTful API for user authentication and chat
functionality.

## Project Overview

This project is a chatbot application built using Django and Django Rest Framework. It includes user authentication
using JWT (JSON Web Tokens) and provides endpoints for user registration, login, logout, and chat interactions.

## Setup Instructions

1. Clone the repository:
   Apply
   git clone https://github.com/your-username/AI_chat.git

2. Navigate to the project directory:
   Apply
   cd AI_chat

3. Create and activate a virtual environment:
   Apply
   python -m venv .venv
   source .venv/bin/activate # On Windows, use: .venv\Scripts\activate

4. Install the required dependencies:
   Apply
   pip install -r requirements.txt

5. Apply database migrations:
   Apply
   python manage.py migrate

6. Run the development server:
   Apply
   python manage.py runserver

## API Endpoints


### User Authentication

### Register

- **URL:** `/api/signup/`
- **Method:** POST
- **Description:** Register a new user
- **Request Body:**
``` json
{
  "username": "string"
 "password": "string",
 "email": "string"
}
```
- **Response**
``` json
{
 "message": success/failure
 "access": jwt_access_token
}
```
### Login

- **URL:** `/api/login/`
- **Method:** POST
- **Description:** Register a new user
- **Request Body:**

``` json 
{
   "username": "{username}",
   "password": "{password}"
}
```
### Chat

- **URL:** `/api/chat/`
- **Method:** POST
- **Description:** talk with the AI 
- **Request Body:**

``` json 
{
   "chat": "your conversation message goes here"
}
```
In addition, add the access token you receive from the login to the authentication header to get access to this and other non authentication services

### Get token balance

- **URL:** `/api/tokenbalance/`
- **Method:** GET
- **Description:** check how many tokens are left in user's account 

### Transfer token

- **URL:** `/api/tokentransfer/`
- **Method:** POST
- **Description:** talk with the AI 
- **Request Body:**
```json
{
   "recipient": "{recipient username}",
   "amount": "{amount to be transferred}",
}
```
## This is it for now but this is not it forever. 
### future plans for this project
- making the chat with a real AI instead of just a dummy text message
- session tracking that relates consecutive chats to the different sessions a user has and displays it as such so that users can access their previous chats
- sharing of chats between users for collaborative work and common environments
- front end ui to make the app reach more people
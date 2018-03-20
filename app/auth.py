from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from datetime import timedelta

## In-house imports 
from . import app
from models.User import user_table

# CONFIGURATION FOR Flask-JWT
app.config['SECRET_KEY']            = 'super-secret'
app.config['JWT_EXPIRATION_DELTA']  =  timedelta(seconds=1800)
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_AUTH_URL_RULE']     = '/login'

def login(email, password):
    user = user_table.get(email, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return user_table.get(user_id, None)

def main():
    print login("r2d2@sw.com", "iamr2d2")
    print login("r2d2@sw.com", "WrongPassword")

if __name__ == '__main__':
    main()
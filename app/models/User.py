#-------------------------------------------------------------------------------
# Name:        User.py
# Purpose:     Model class for users
# Author(s):   Farhan Hussain
#-------------------------------------------------------------------------------

class UserModel(object):
    def __init__(self, email, password, roles=[]):
        self.email      = email
        self.password   = password
        self.roles      = roles

    def __str__(self):
        return "User(email='%s')" % self.email

    def get_user(self, email):
        return { k:v for k,v in users if v == email }


""" REMEMBER - ONLY for testing / DEMO """
users = [
    UserModel("r2d2@sw.com", "iamr2d2", ['admin', 'developer']),
    UserModel("bb8@sw.com", "tewntewn", ['developer']),
]
user_table      = { u.email: u for u in users }
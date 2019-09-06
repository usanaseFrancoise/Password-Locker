import pyperclip
from user_cred import User, Credential

def create_user(fname,lname,password):
    '''
    function to create a new user account
    '''
    new_user= User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    function to save user account
    '''
    User.save_user(user)

def verify_user(first_name,password):
    '''
    function that verifies the existance of user
    '''
    checking_user = Credential.check_user(first_name,password)
    return checking_user

def generate_password():
    '''
    function to create new credential
    '''
    new_credential=Credential(user_name,site_name,account_name,password)
    return new_credential
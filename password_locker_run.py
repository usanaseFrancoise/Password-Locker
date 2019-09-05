from user_credentials import user, user_credentials
def create_user(fname,lname,email,password):
    '''
    function to create a new user account
    '''
    new_user = User(fname,lname,email,password)
    return new_user

def save_user(user):
    '''
    function to save a new user account
    '''
    user.save_user(user)
def verify_user(first_name,password):
    '''
    function that verifies the existance user
    '''
    checking_user= Credential.check_user(first_name,password)
    return check_user
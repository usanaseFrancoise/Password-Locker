class User:
    """
    class to create user account
    """
    users_list=[]
    def __init__(self,first_name,last_name,email,password):
        '''
        defining the object for each user
        '''
        #instance variable
        
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
    def save_user(self):
        '''
		Function to save a newly created user instance
		'''
        User.users_list.append(self)
        pass
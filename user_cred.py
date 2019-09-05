import string

class User:
    '''
    class to create user account
    '''
    users_list=[]
    def __init__(self,first_name,last_name,password):
        '''
        method to define the properties for each object
        '''
        self.first_name=first_name
        self.last_name=last_name
        self.password=password

    def save_user(self):
        '''
        function to save a anew created user instance
        '''
        User.users_list.append(self)

class  Credential:
    '''
    class to create account credentials ,generate password
    '''
    credentials_list=[]
    user_credentials_list=[]
    @classmethod
    def check_user(cls,first_name,password):
        '''
        method that checks if the name and password matches
        '''
        current_user=''
        for user in User.users_list:
            if(user.first_name == first_name and password ==password):
                current_user = user.first_name
        return current_user
    def __init__(self,user_name,site_name,account_name,password):
        '''
        method to define the properties of user
        '''
        self.user_name= user_name
        self.site_name=site_name
        self.account_name=account_name
        self.password=password
    def save_credential(self):
        '''
        function to save credentials 
        '''
        Credential.credentials_list.append(self)

    def genereate_password(sixe=8,char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        function to generate an 8 character password
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass
    @classmethod
    def display_credentials(cls,user_name):
        '''
		Class method to display the list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list
				

	
    @classmethod
    def find_by_site_name(cls, site_name):
        '''
		Method that takes in a site_name and returns a credential that matches that site_name.
		'''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def copy_credential(cls,site_name):
        '''
		Class method that copies a credential's info after the credential's site name is entered
        '''
        find_credential = Credential.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)

       
				

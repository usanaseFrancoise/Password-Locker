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
    function to generate password
    '''
    gen_pass = Credential.generate_password()
    return gen_pass  

def create_credential(user_name,site_name,account_name,password):
    '''
    function to create new credential
    '''
    new_credential=Credential(user_name,site_name,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    function to save credential
    '''
    Credential.save_credential(credential)

def display_credentials(user_name):
    '''
    function to display credential saved
    '''
    return Credential.display_credentials(user_name)

def copy_credential(site_name):
    '''
    function to copy credential
    '''
    return Credential.copy_credential(site_name)

def main():
    print(' ')
    print('welcome to password Locker!')
    while True:
            print(' ')
            print("_"*80)
            print('use this code to perfom specific task you want :\n cc -Create Account \n log -Log In \n ex -Exit ')
            short_code = input('Enter a choice: ').lower().strip()
            if short_code == 'ex':
                break
            elif short_code == 'cc':
                print("_"*80)
                print(' ')
                print('to create a new account:')
                first_name = input('Enter your first_name - ').strip()
                last_name = input('Enter your last_name - ').strip()
                password= input('Enter your password - ').strip()
                save_user(create_user(first_name,last_name,password))
                print(" ")
                print(f'New Acoount created for: {first_name}{last_name} using password: {password}')

            elif short_code == 'log':
                print("_"*80)
                print(' ')
                print('to login enter your account details:')
                user_name = input('Enter your first_name - ').strip()
                password= str(input('Enter your password - '))
                user_exists = verify_user(user_name,password)
                if user_exists == user_name:
                    print(" ")
                    print(f'Welcome {user_name} .Please choose any option  to continue.')
                    print(' ')  
                    while True:
                        print("_"*80)
                        print('to navigate to credential account use code:\n cc-create account \n dc- display Credentials \n copy- copy  password \n  ex- Exit')
                        short_code=input('Enter a choice: ').lower().strip()
                        print("_"*80)
                        if short_code =='ex':
                            print(' ')   
                            print(f'Thank you! {user_name}.')
                            break
                        elif short_code =='cc':
                            print(' ')
                            print('Enter your credential: ')
                            site_name = input('enter the site\'s name- ').strip() 
                            account_name = input('enter your account \'s name - ').strip()
                            
                            while True:
                                print(' ')
                                print("_"*80)
                                print("please enter the choose for entering password for credential: \n exp-enter existing password \n gp-generate password \n ex- Exit")
                                psw_choice = input('Enter an option: ').lower().strip()
                                print("-"*80)
                                if psw_choice == 'exp':
                                    print(" ")
                                    password = input('enter your password: ').strip()
                                    break
                                elif psw_choice == 'gp':
                                    password = generate_password()
                                    break
                                elif psw_choice == 'ex':
                                    break
                                else:
                                    print('Try Again!.')
                            save_credential(create_credential(user_name,site_name,account_name,password))
                            print(' ')
                            print(f'Credential Created:Site Name:{site_name} -Acount Name:{account_name} -Password:{password}')
                            print(' ')
                        elif short_code == 'dc':
                            print(' ')
                            if display_credentials(user_name):
                                print('Here is a list of all credentials')
                                print(' ')
                                for credential in display_credentials(user_name):
                                    print(f'Site Name:{credential.site_name} -Account Name:{credential.account_name} - Password: {credential.password}')
                                    print(' ')
                            else:
                                print(' ')
                                print("you don't seem to have any crdential")
                                print(' ')
                    
                        elif short_code =='copy':
                            print(' ')
                            chosen_site = input("enter the site for credential password to copy")
                            copy_credential(chosen_site)
                            print(' ')
                        else: 
                            print('TRY Again')
                
                else:
                    print(' ')
                    print('TRY Again or create another account.')

                 
         
            else:
                print("_"*80)
                print(' ')
                print("try Again")



if __name__ == '__main__':
    main()





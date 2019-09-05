import unittest
from user_cred import User
class TestUser(unittest.TestCase):
    '''
    Test class that define the user behaviours
    '''
    def setUp(self):
        '''
        function to create user account
        '''
        self.new_user=User('fanny','usanase','fanny@gmail.com','123')
    def test__init__(self):
        '''
        to check if new users information is saved
        '''

        self.assertEqual(self.new_user.first_name,"fanny")
        self.assertEqual(self.new_user.last_name,"usanase")
        self.assertEqual(self.new_user.email,"fanny@gmail.com")
        self.assertEqual(self.new_user.password,"123")

    def test__init__(self):   
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
if __name__ == '__main__':
    unittest.main()
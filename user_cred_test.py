import unittest
import pyperclip
from user_cred import User, Credential

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('fanny','usanase','fa100')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of user instances is properly done
		'''
		self.assertEqual(self.new_user.first_name,'fanny')
		self.assertEqual(self.new_user.last_name,'usanase')
		self.assertEqual(self.new_user.password,'fa100')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),2)

	def test_delete_account(self):
		'''
		delete account
		'''
		self.new_user.save_user()
		test_user=User("Test","user","password")
		test_user.save_user()
		self.new_user.delete_user()
		self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('fanny','usanase','fa100')
		self.new_user.save_user()
		user2 = User('mimi','mutoni','mi00')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))


	

	






	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential('fanny','Facebook','fannyusanase','fa100')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'fanny')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'fannyusanase')
		self.assertEqual(self.new_credential.password,'fa100')

	def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credential()
		twitter = Credential('Jane','Twitter','dukundane','d100')
		twitter.save_credential()
		self.assertEqual(len(Credential.credentials_list),2)

	

	def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential. save_credential()
		twitter = Credential('Jane','Twitter','dukundane','d100')
		twitter. save_credential()
		gmail = Credential('Jane','Gmail','dukundane','d200')
		gmail. save_credential()
		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

	def test_find_by_site_name(self):
		'''
		Test to check if the find_by_site_name method returns the correct credential
		'''
		self.new_credential.save_credential()
		twitter = Credential('Jane','Twitter','dukundane','d100')
		twitter.save_credential()
		credential_exists = Credential.find_by_site_name('Twitter')
		self.assertEqual(credential_exists,twitter)
	def test_copy_credential(self):
		'''
		test to chech if the copy a credetion methhod copies the correct credetions
		'''
		self.new_credential.save_credential()
		twitter=Credential('jane','Twitte','dukundane','d100')
		twitter.save_credential()
		find_credential = None

		for credential in Credential.user_credentials_list:
			find_credential=Credential.find_by_site_name(credential.site_name)
			return pyperclip.copy(find_credential.password)

		Credential.copy_credential(self.new_credential.site_name)
		self.assertEqual('fa100',pyperclip.paste())
		print(pyperclip.paste())
		

if __name__ == '__main__':
	unittest.main()
	# unittest.main(verbosity=2)
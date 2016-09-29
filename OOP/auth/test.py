import unittest
from user import User
from auth import Authenticator,Authorizor
class UserTest(unittest.TestCase):
	"""docstring for UserTest"""
	def setUp(self):
		self.user = User("joe","joepassword")
    
	def test_checkpassword(self):
		self.assertTrue(self.user.check_password("joepassword"))

class AuthenticatorTest(unittest.TestCase):
	def setUp(self):
		self.authenticator = Authenticator()
		self.authenticator.add_user("joe","joepassword")
	@unittest.skip("this is useless")
	def test_add_user(self):
		self.authenticator.add_user("joe","joepassword")
		self.assertTrue("joe" in self.authenticator.users.keys())
	def test_login(self):
		self.assertTrue(self.authenticator.login("joe","joepassword"))

class AuthorizorTest(unittest.TestCase):
	"""docstring for AuthorizorTest"""
	def setUp(self):
		self.authenticator = Authenticator()
		self.authenticator.add_user("joe","joepassword")
		self.authenticator.login("joe","joepassword")
		self.authorizor = Authorizor(self.authenticator)
		self.authorizor.add_permission("paint")
	@unittest.skip("this is useless")
	def test_add_permission(self):
		self.authorizor.add_permission("paint")
		self.assertTrue("paint" in self.authorizor.permissions.keys())
	def test_check_permission(self):
		self.authorizor.permit_user("paint","joe")
		self.authorizor.check_permission("paint","joe")

if __name__ == '__main__':
	unittest.main()
from myException import *
from user import User
class Authenticator():
	"""docstring for Authenticator"""
	def __init__(self):
		self.users = {}

	def add_user(self,username,password):
		if username in self.users:
			raise UsernameAlreadyExists(username)
		if len(password) < 6:
			raise PasswordTooShort(username)
		self.users[username] = User(username,password)
	def login(self,username,password):
		try:
			user = self.users[username]
		except KeyError:
			raise InvalidUsername(username)
		if not user.check_password(password):
			raise InvalidPassword(username,password)
		user.is_logged_in = True
		return True
	def is_logged_in(self,username):
		if username in self.users:
			return self.users[username].is_logged_in
		return False
authenticator = Authenticator()
class Authorizor:
	"""docstring for Authorizor"""
	def __init__(self, authenticator):
		self.authenticator = authenticator
		self.permissions = {}

	def add_permission(self,perm_name):
		try:
			perm_set = self.permissions[perm_name]
		except KeyError:
			self.permissions[perm_name] = set()
		else:
			raise PermissionError("permission exists")
	def permit_user(self,perm_name,username):
		try:
		    perm_set = self.permissions[perm_name]
		except KeyError:
			raise PermissionError("Permission does not exist")
		else:
			if username not in self.authenticator.users:
				raise InvalidUsername(username)
			perm_set.add(username)
           
	def check_permission(self,perm_name,username):
		if not self.authenticator.is_logged_in(username):
			raise NotLoggedInError
		try:
			perm_set = self.permissions[perm_name]
		except KeyError:
			raise PermissionError("Permission does not exist")
		else:
			if username not in perm_set:
				raise NotPermittedError(username)
			else:
				return True




		


		
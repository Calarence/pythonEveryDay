class AuthException(Exception):
	"""docstring for AuthException"""
	def __init__(self, username,user=None):
		super().__init__(username,user)
		self.username = username
		self.user = user

		
class UsernameAlreadyExists(AuthException):
	"""docstring for UsernameAlreadyExists"""
	pass

class PasswordTooShort(AuthException):
	"""docstring for PasswordTooShort"""
	pass
class InvalidUsername(AuthException):
	pass
class InvalidPaasword(AuthException):
	pass
class NotLoggedInError(AuthException):
	pass
class NotPermittedError(AuthException):
	pass
	
class PermissionError(Exception):
	pass

		
		
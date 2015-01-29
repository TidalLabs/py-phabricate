from phabricator import Phabricator as _Phabricator

class Phabricator(_Phabricator):
	def get_user(self, alias):
		"""
		Utility to fetch a single user's data by alias
		"""
		return self.user.find(aliases=[alias,])

	def get_user_id(self, alias):
		"""
		API returns user ID in an attribute named by the alias
		Which is of course a giant PITA to access.
		"""
		user = self.get_user(alias)
		return getattr(user, alias)

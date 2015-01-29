from phabricator import Phabricator as _Phabricator

class Phabricator(_Phabricator):
	"""
	Wrapper class for phabricator.Phabricator from python-phabricator.
	Provides convenience methods for easier access to queries and attributes
	that are awkward with python-phabricator due to Conduit quirks.
	"""

	def get_user(self, alias):
		"""
		Utility to fetch a single user's data by username

		@param str alias	The username of the user you want to fetch
		@return Result		python-phabricator Result object containing user data
		"""
		return self.user.find(aliases=[alias,])

	def get_user_id(self, alias):
		"""
		API returns user ID in an attribute named by the alias
		Which is of course a giant PITA to access.

		@param str alias	The username of the user you want to fetch
		@return str 		The Phabricator id ("phid") of the user in question
		"""
		user = self.get_user(alias)
		return getattr(user, alias)

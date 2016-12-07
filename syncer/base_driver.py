class BaseSyncDriver:
	"""
	Base sync driver

	Ever driver should follow one simple route to work

	1. Initialize
	2. Authenticate itself to provider
	3. Call APIs multiple times as data required and collect locally
	4. Update db with new data

	More objects can work in parallel to achieve more performance
	"""

	def __init__(ep_name, *args, **kwargs):
		self.ep_name = ep_name
		

	def call_api(url, method='GET', payload=None):
		pass

	def update_db():
		pass

	def authenticate():
		pass

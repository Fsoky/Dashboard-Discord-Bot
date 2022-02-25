import aiohttp
import config


class Oauth2:

	@staticmethod
	def login():
		return f"{config.DEFAULT_URL}/oauth2/authorize?client_id={config.CLIENT_ID}&redirect_uri={config.REDIRECT_URI}&response_type=code&scope={config.SCOPES}"

	@staticmethod
	async def get_access_token(code):
		payload = {
			"client_id": config.CLIENT_ID,
			"client_secret": config.CLIENT_SECRET,
			"grant_type": "authorization_code",
			"code": code,
			"redirect_uri": config.REDIRECT_URI,
			"scope": config.SCOPES
		}

		async with aiohttp.ClientSession() as session:
			async with session.post(f"{config.DEFAULT_URL}/oauth2/token", data=payload) as response:
				obj = await response.json()
				return obj["access_token"]

	@staticmethod
	async def get_user(access_token):
		headers = {"Authorization": f"Bearer {access_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(f"{config.DEFAULT_URL}/users/@me", headers=headers) as response:
				obj = await response.json()
				return obj
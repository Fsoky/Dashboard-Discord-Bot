from flask import Flask, request, redirect # pip install Flask[async]
from oauth2 import Oauth2

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
	return redirect(Oauth2.login())


@app.route("/login", methods=["GET"])
async def login():
	code = request.args.get("code")
	access_token = await Oauth2.get_access_token(code)

	user = await Oauth2.get_user(access_token)
	return f"{user['username']}#{user['discriminator']}"


if __name__ == '__main__':
	app.run(debug=True)
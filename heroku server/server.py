import os
from bottle import Bottle, route, run, HTTPResponse
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
sentry_sdk.init(
    dsn="https://31bf58781cf04930bbabf64fb6a92de1@o479964.ingest.sentry.io/5525983",
    integrations=[BottleIntegration()]
)
app = Bottle()
@app.route("/success")
def success():
	raise HTTPResponse(status=200,body="все прошло успешно")
@app.route("/fail")
def fail():
	raise RuntimeError("Error to check")
if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
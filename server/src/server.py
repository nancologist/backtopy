from sanic import Sanic
from sanic.response import json

# Fake DB =========================
data = [
    # status:
    {
        "id": "js32d",
        "author": "John",
        "text": 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren'
    },
    {
        "id": 'xmk32',
        "author": 'Sarah',
        "text": "no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr"
    }
]
# =================================

app = Sanic("backtopy")

@app.route("/")
async def index(request):
    return json({"hello": "world"})

@app.route("/statuses")
async def index(request):
    return json(data, indent=2)

@app.middleware("response")
async def allow_cors(request, response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    response.headers["Access-Control-Allow-Methods"] = "OPTIONS, GET, POST, PUT, PATCH, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"


if __name__ == "__main__":
    app.run()
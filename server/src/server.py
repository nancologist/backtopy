from sanic import Sanic
from sanic.response import json



app = Sanic("app_server_2021")

@app.route('/')
async def index(request):
    return json({"hello": "world"})

@app.post('/test')
async def get_test(req):
    print(req.json)
    return json({"msg": "ok"})

if __name__ == "__main__":
    app.run() 
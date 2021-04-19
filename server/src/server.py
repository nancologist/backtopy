from sanic import Sanic
from sanic.response import json
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from models.status import Status

# ElasticSearch ===================
connections.create_connection(hosts=["localhost"])
Status.init()

# =================================

app = Sanic("status-app")

@app.route("/")
async def test(request):
    return json({"hello": "world"})


@app.get("/statuses")
async def get_statuses(request):
    s = Search(index="status_index")
    statuses = s.execute().to_dict()["hits"]["hits"]
    return json(statuses, indent=2)


@app.post("/status")
async def add_status(request):
    new_status = request.json
    return json({"msg": "ok"})


@app.middleware("response")
async def allow_cors(request, response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    response.headers["Access-Control-Allow-Methods"] = "OPTIONS, GET, POST, PUT, PATCH, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "content-type, authorization"

app.run()
from sanic import Sanic
from sanic.response import json
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from models.status import Status

# ElasticSearch ===================
connections.create_connection(hosts=["localhost"])
Status.init()

# =================================

app = Sanic("backtopy")


@app.route("/")
async def index(request):
    return json({"hello": "world"})


@app.route("/statuses")
async def index(request):
    s = Search(index="status_index")
    statuses = s.execute().to_dict()["hits"]["hits"]
    return json(statuses, indent=2)


@app.middleware("response")
async def allow_cors(request, response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    response.headers["Access-Control-Allow-Methods"] = "OPTIONS, GET, POST, PUT, PATCH, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

app.run()
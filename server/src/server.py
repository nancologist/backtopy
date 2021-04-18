from sanic import Sanic
from sanic.response import json
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from models.status import Status

# ElasticSearch ===================
connections.create_connection(hosts=["localhost"])
Status.init()

s = Search(index="status_index")
hits = s.execute()
for hit in hits:
    print(hit.meta.id, hit.title)

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

app.run()
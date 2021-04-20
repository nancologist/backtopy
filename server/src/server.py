from sanic import Sanic
from sanic.response import json, empty
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from models.status import Status

# ElasticSearch
connections.create_connection(hosts=["localhost"])
Status.init()

app = Sanic("status-app")

@app.route("/")
async def test(req):
    return json({"hello": "world"})


@app.get("/statuses")
async def get_statuses(req):
    s = Search(index="status_index")
    statuses = s.execute().to_dict()["hits"]["hits"]
    return json(statuses, indent=2)


@app.post("/status")
async def add_status(req):
    new_status = Status(
        title=req.json.get("title"),
        text=req.json.get("text")
    )
    new_status.save()
    return json({}, status=201)


@app.put("/status")
async def update_status(req):
    status = Status.get(id=req.json.get("id"))
    status.title = req.json.get("title")
    status.text = req.json.get("text")
    status.save()
    return json({})


@app.delete("/status/<status_id>")
async def delete_status(req, status_id):
    status = Status.get(id=status_id)
    status.delete()
    return json({})


@app.middleware("request")
async def handle_preflight_reqs(req):
    if req.method == "OPTIONS":
        return empty()


@app.middleware("response")
async def allow_cors(req, res):
    res.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    res.headers["Access-Control-Allow-Methods"] = "OPTIONS, GET, POST, PUT, PATCH, DELETE"
    res.headers["Access-Control-Allow-Headers"] = "content-type, authorization"

app.run()
# BackToPy

## 1. Server (Sanic)

### 1.1. Run
1. `cd server/`
2. `pip install -r requirements.txt`
3. `source env/bin/activate`
4. `cd src/`
5. `sanic server.app`

### 1.2. Dependencies
* [Sanic](https://sanicframework.org/)

___

## 2. Database (Elasticsearch)

### 2.1. Run
1. `docker pull elasticsearch:7.12.0`
2. `docker network create <NETWORK-NAME>`
3. `docker run -d --name elasticsearch --net <NETWORK-NAME> -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.12.0`

___

## 3. Client (VueJS)

### 3.1. Run
1. `cd client/`
2. `npm install`
3. `npm start`

### 3.2. Dependencies
* Vue CLI
* Axios
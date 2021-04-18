from datetime import datetime
from elasticsearch_dsl import Document, Date, Text
from elasticsearch_dsl.connections import connections

class Status(Document):
    title = Text()
    text = Text()
    created_at = Date()

    class Index:
        name = "status_index"
    
    def save(self, ** kwargs):
        return super(Status, self).save(** kwargs)
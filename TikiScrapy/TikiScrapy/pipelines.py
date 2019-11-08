# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class TikiscrapyPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "mongodb://asama:12345678a@cluster0-shard-00-00-oszst.mongodb.net:27017,cluster0-shard-00-01-oszst.mongodb.net:27017" +
    ",cluster0-shard-00-02-oszst.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
        )
        db = self.conn["test"]
        self.collection = db["quotes_tb"]

    def process_item(self, item, spider):
        #self.collection.insert(dict(item))
        return item

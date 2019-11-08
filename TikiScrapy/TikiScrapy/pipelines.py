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
        list_title = item["title"]
        list_product_id = item["product_id"]
        list_data_id = item["data_id"]
        list_image = item["image"]
        list_final_price = item["final_price"]
        list_price_regular = item["price_regular"]
        list_discount = item["discount"]
        list_link = item["link"]
        results = list()
        for i in range(len(list_title)):
            sp_dict = dict()
            sp_dict["title"] = list_title[i]
            sp_dict["product_id"] = list_product_id[i]
            sp_dict["data_id"] = list_data_id[i]
            sp_dict["image"] = list_image[i]
            sp_dict["final_price"] = list_final_price[i]
            sp_dict["price_regular"] = list_price_regular[i]
            sp_dict["discount"] = list_discount[i]
            sp_dict["link"] = list_link[i]

            results.append(sp_dict)

        self.collection.insert(results)
        return item

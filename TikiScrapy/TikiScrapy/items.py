# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TikiscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    product_id = scrapy.Field()
    data_id = scrapy.Field()
    image = scrapy.Field()
    final_price = scrapy.Field()
    price_regular = scrapy.Field()
    discount = scrapy.Field()
    link = scrapy.Field()

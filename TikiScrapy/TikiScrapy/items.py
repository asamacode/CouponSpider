# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CouponItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    shop_name = scrapy.Field()
    description = scrapy.Field()
    date_end = scrapy.Field()
    voucher = scrapy.Field()
    link = scrapy.Field()

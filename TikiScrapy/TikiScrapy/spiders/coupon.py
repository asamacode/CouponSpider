import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TikiScrapy.items import CouponItem
from urllib.parse import unquote
import re
from slugify import slugify

from bson import ObjectId

FILE_PATH = 'coupon_links.txt'


def read_list_from_file(path):
    list_of_start_urls = []
    for line in open(path, 'r'):
        list_of_start_urls.append(line.strip())
    return list_of_start_urls


def strip_value(value):
    m = re.search("http[^\s]+(\s)*h?(http[^\s>]+)(\s)*", value)
    if m:
        # print m.group(2).encode('UTF-8')
        return m.group(2)
    else:
        # print value.encode('UTF-8')
        return value


def price_to_int(price):
    m = ''.join([d for d in price if d.isdigit()])
    return int(m)


class CouponSpider(scrapy.Spider):
    name = 'coupon1'
    list_of_start_urls = read_list_from_file(FILE_PATH)

    allowed_domains = ['magiamgia.com']
    start_urls = list_of_start_urls

    # start_urls = ['https://magiamgia.com/ma-giam-gia/sendo/',]

    def parse(self, response):
        urls = response.xpath('//div[@class="content-voucher"]/h3[@class="title clear"]//a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        print('Parse Item>>>>>>>>>>>>>>>>>>>>>')
        i = CouponItem()

        try:
            i['title'] = response.xpath('//h1[@class="title"]//text()').extract()[0].strip()
        except Exception:
            i['title'] = ""

        try:
            i['date_end'] = response.xpath('//div[@class="date-end"]//text()[2]').extract()[0].strip()
        except:
            i['date_end'] = ""

        try:
            i['voucher'] = response.xpath('//div[@class="code-full-detail"]/input/@value').extract()[0].strip()
        except:
            i['voucher'] = ""

        try:
            i['link'] = unquote(
                response.xpath('//div[@class="wrap-single-cp"]//a/@href | //div[@class="btn-cart"]/a/@href').extract()[
                    0].strip().split("?url=", 1)[1])
        except:
            i['link'] = ""

        try:
            i['description'] = response.xpath('//div[@class="content-category mona-content"]/p[2]//text()').extract()[
                0].strip()
        except:
            i['description'] = ""

        if "sendo" in i['link']:
            i['shop_name'] = "sendo"
        if "shopee" in i['link']:
            i['shop_name'] = "shopee"
        if "tiki" in i['link']:
            i['shop_name'] = "tiki"
        if "lazada" in i['link']:
            i['shop_name'] = "lazada"
        if "adayroi" in i['link']:
            i['shop_name'] = "adayroi"
        if "mytour" in i['link']:
            i['shop_name'] = "mytour"
        if "grab" in i['link']:
            i['shop_name'] = "grab"
        if "yes24" in i['link']:
            i['shop_name'] = "yes24"
        if "lotte" in i['link']:
            i['shop_name'] = "lotte"
        if "didongviet" in i['link']:
            i['shop_name'] = "didongviet"
        if "klook" in i['link']:
            i['shop_name'] = "klook"
        if "couple-tx" in i['link']:
            i['shop_name'] = "couple-tx"
        if "fahasa" in i['link']:
            i['shop_name'] = "fahasa"
        if "nguyen-kim" in i['link']:
            i['shop_name'] = "nguyen-kim"
        if "fado" in i['link']:
            i['shop_name'] = "fado"
        if "aeon" in i['link']:
            i['shop_name'] = "aeon"
        if "fpt" in i['link']:
            i['shop_name'] = "fpt"
        if "cellphones" in i['link']:
            i['shop_name'] = "cellphones"
        if "goviet" in i['link']:
            i['shop_name'] = "goviet"
        if "usexpress" in i['link']:
            i['shop_name'] = "usexpress"
        if "agoda" in i['link']:
            i['shop_name'] = "agoda"
        if "ifitness" in i['link']:
            i['shop_name'] = "ifitness"
        if "vua-bia" in i['link']:
            i['shop_name'] = "vua-bia"
        if "vietravel" in i['link']:
            i['shop_name'] = "vietravel"
        if "hnam-mobile" in i['link']:
            i['shop_name'] = "hnam-mobile"
        if "now" in i['link']:
            i['shop_name'] = "now"
        if "laneige" in i['link']:
            i['shop_name'] = "laneige"
        if "the-face-shop" in i['link']:
            i['shop_name'] = "the-face-shop"
        if "vinabook" in i['link']:
            i['shop_name'] = "vinabook"
        if "mia" in i['link']:
            i['shop_name'] = "mia"
        if "shop-vnexpress" in i['link']:
            i['shop_name'] = "shop-vnexpress"
        if "unica" in i['link']:
            i['shop_name'] = "unica"
        if "bestprice" in i['link']:
            i['shop_name'] = "bestprice"
        if "be" in i['link']:
            i['shop_name'] = "be"
        if "lalamove" in i['link']:
            i['shop_name'] = "lalamove"
        if "juno" in i['link']:
            i['shop_name'] = "juno"
        if "aliexpress" in i['link']:
            i['shop_name'] = "aliexpress"
        yield i

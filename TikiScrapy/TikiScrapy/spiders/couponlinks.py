import scrapy
from scrapy.selector import Selector

import re
from  urllib import parse

FILE_PATH = 'coupon_links.txt'

def format_link(url):
	if not url.startswith('http://magiamgia.com/'):
		url = parse.urljoin('http://magiamgia.com/', url)
		# print url
	return url

def append_to_file(path, url):
	with open(path, 'a') as f:
		if url != 'javascript:void(0);':
			f.write(url + "\n")

class CouponLinkSpider(scrapy.Spider):
    name = "couponlink"
    allowed_domains = ["magiamgia.com"]
    start_urls = (
        'http://magiamgia.com/',
    )

    def parse(self, response):
        links = Selector(response).xpath('//ul[@class="coupon-category-grid"]/li/a/@href')
        for link in links:
            url = link.extract()
            url = format_link(url)

            append_to_file(FILE_PATH, url)

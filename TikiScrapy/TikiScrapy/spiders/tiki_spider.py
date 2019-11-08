import scrapy
from ..items import TikiscrapyItem

class TikiSpider(scrapy.Spider) :
    name = "tiki"
    page_number = 2
    start_urls = [
        #'https://tiki.vn/dien-thoai-may-tinh-bang/c1789/xiaomi?src=c.1789.hamburger_menu_fly_out_banner',
        'https://tiki.vn/dien-thoai-may-tinh-bang/c1789/apple?src=mega-menu'
    ]

    def parse(self, response):

        items = TikiscrapyItem()

        allsp = response.xpath("//div[@class='product-box-list']")
        for sp in allsp :
            title = sp.xpath("//div/@data-title").extract()
            product_id = sp.xpath("//div/@data-seller-product-id").extract()
            data_id = sp.xpath("//div/@data-id").extract()
            image = sp.xpath("//div[@class='content ']//span[@class='image']//img/@src").extract()
            final_price = sp.xpath("//div/@data-price").extract()
            price_regular = sp.xpath("//div[@class='content ']//p[@class='price-sale']//span[@class='price-regular']/text()").extract()
            discount = sp.xpath("//div[@class='content ']//p[@class='price-sale']//span[@class='sale-tag sale-tag-square']/text()").extract()
            link = sp.xpath("//div[@class='product-item    ']//a/@href").extract()

            items["title"] = title
            items["product_id"] = product_id
            items["data_id"] = data_id
            items["image"] = image
            items["final_price"] = final_price
            items["price_regular"] = price_regular
            items["discount"] = discount
            items["link"] = link

            yield items

        #next_page = "https://tiki.vn/dien-thoai-may-tinh-bang/c1789/xiaomi?src=c.1789.hamburger_menu_fly_out_banner&page=" + str(TikiSpider.page_number)
        next_page = "https://tiki.vn/dien-thoai-may-tinh-bang/c1789/apple?src=mega-menu&page="+ str(TikiSpider.page_number)

        if TikiSpider.page_number <= 3:
            TikiSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse)
import scrapy
from ..items import TikiscrapyItem
class TikiSpider(scrapy.Spider) :
    name = "tiki"
    page_number = 2
    start_urls = [
        'https://tiki.vn/dien-thoai-may-tinh-bang/c1789/xiaomi?src=c.1789.hamburger_menu_fly_out_banner',
    ]

    def parse(self, response):

        items = TikiscrapyItem()
       # title = response.xpath("//div[@class='content ']/p[@class='title']").extract()
        allsp = response.xpath("//div[@class='product-box-list']")
        for sp in allsp :
            items["title"] = sp.xpath("//div/@data-title").extract()
            items["product_id"] = sp.xpath("//div/@data-seller-product-id").extract()
            items["data_id"] = sp.xpath("//div/@data-id").extract()
            items["image"] = sp.xpath("//div[@class='content ']//span[@class='image']//img/@src").extract()
            items["final_price"] = sp.xpath("//div/@data-price").extract()
            items["price_regular"] = sp.xpath("//div[@class='content ']//p[@class='price-sale']//span[@class='price-regular']/text()").extract()
            items["discount"] = sp.xpath("//div[@class='content ']//p[@class='price-sale']//span[@class='sale-tag sale-tag-square']/text()").extract()
            items["link"] = sp.xpath("//div[@class='product-item    ']//a/@href").extract()
            yield items

        next_page = "https://tiki.vn/dien-thoai-may-tinh-bang/c1789/xiaomi?src=c.1789.hamburger_menu_fly_out_banner&page=" + str(TikiSpider.page_number)

        if TikiSpider.page_number <= 3:
            TikiSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse)
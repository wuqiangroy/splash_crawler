"""
这是一个示例，用来爬取 ajax 的京东商品信息
"""

from scrapy import Spider, Request, Selector
from scrapy.conf import settings


class JingDongSpider(Spider):

    name = "jingdong_phone_price"

    def start_requests(self):
        url = "https://list.jd.com/list.html?cat=9987,653,655"

        yield Request("http://{}:8050/render.html?url={}".format(settings["SPLASH_URL"], url), callback=self.parse)

    def parse(self, response):
        data = []
        res = response.xpath("//li[@class='gl-item']").extract()
        for i in res:
            name = Selector(text=str(i)).xpath("//div[@class='p-name']//em/text()").extract_first()
            price = Selector(text=str(i)).xpath("//strong[@class='J_price']//i/text()").extract_first()
            data.append({name.strip("\n\t "): price})
        return data

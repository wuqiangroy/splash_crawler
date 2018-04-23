"""
这是个一个示例，演示 ajax 加载的今日头条的新闻数据
"""
from scrapy import Spider, Request, Selector


class JinRiTouTiaoSpider(Spider):
    name = "jinritoutiao_news"

    def start_requests(self):
        url = "https://www.toutiao.com/"
        yield Request("http://localhost:8050/render.html?url={}".format(url), callback=self.parse)

    def parse(self, response):
        data = []
        res = response.xpath("//li[@class='article-item']").extract()
        for i in res:
            title = Selector(text=str(i)).xpath("//p[@class='module-title']/text()").extract_first()
            url = Selector(text=str(i)).xpath("//a/@href").extract_first()
            data.append({title: url})
        return data

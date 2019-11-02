import scrapy

from yikuman.items import YikumanItem


class YikumanList(scrapy.Spider):
    name = 'yikumanlist'
    allowed_domains = ['yikuman.com']
    start_urls = ['https://yikuman.com/category/page/1']

    # def start_requests(self):

    def parse(self, response):
        posts = response.xpath("//li[@class='post box row ']")
        for index, post in enumerate(posts):
            img = post.xpath("div[@class='thumbnail']/a/img/@src")
            href = post.xpath("div[@class='article']/h2/a/@href")
            title = post.xpath("div[@class='article']/h2/a/@title")

            date = post.xpath("div[@class='info']/span[@class='info_date info_ico']/text()")
            views = post.xpath("div[@class='info']/span[@class='info_views info_ico']/text()")
            category = post.xpath("div[@class='info']/span[@class='info_category info_ico']/a/text()")

            # print(img.extract_first())
            # print(href.extract_first())
            # print(title.extract_first())
            # print(date.extract_first())
            # print(views.extract_first())
            # print(category.extract_first())
            item = YikumanItem()
            item['title'] = title.extract_first()
            item['date'] = date.extract_first()
            item['comment'] = views.extract_first()
            item['category'] = category.extract_first()
            item['cover'] = img.extract_first()
            item['url'] = href.extract_first()
            item['index'] = item['url'].split("/")[-1].split(".")[0]
            yield item
        pass

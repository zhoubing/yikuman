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
            yield scrapy.Request(item['url'], callback=self.parse_detail, meta={"item": item})
            # yield item

    def parse_detail(self, response):
        item = response.meta['item']
        # print(response.xpath("//div[@id='post_content']/p/br")[0].xpath("following::text()")[0])
        details = response.xpath("//div[@id='post_content']/p//text()")
        detail_name = self.get_text(details, "名称")
        detail_format = self.get_text(details, "格式")
        detail_size = self.get_text(details, "大小")
        detail_time = self.get_text(details, "时间")
        detail_prescription = self.get_text(details, "说明")

        print(detail_name)
        print(detail_format)
        print(detail_size)
        print(detail_time)
        print(detail_prescription)

        detail_img = response.xpath("//div[@id='post_content']/p//img/@src")
        imgs = []
        for img in detail_img:
            imgs.append(img.extract())

        item['detail'] = {
            "name": detail_name,
            "format": detail_format,
            "size": detail_size,
            "time": detail_time,
            "prescription": detail_prescription,
            "imgs": imgs
        }
        print(item)
        yield item

    @staticmethod
    def get_text(li, value):
        for item in li:
            if value in item.extract():
                return item.extract()
        return ""

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class YikumanCoverPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['cover'], meta={'date': item['date']})

    def file_path(self, request, response=None, info=None):
        if request.meta['date']:
            # 这个参数的request就是上面的yield Request.通过meta传递自定义参数
            return request.meta['date'] + "/" + request.url.split('/')[-1]
        else:
            return request.url.split('/')[-1]

    def item_completed(self, results, item, info):
        pass


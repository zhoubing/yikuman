from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class YikumanImagePipeline(object):
    def process_item(self, item, spider):
        return item


class YikumanImgePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        print(results)

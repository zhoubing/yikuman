import pymongo


class YikumanMongoListPipeline(object):

    def open_spider(self, spider):
        self.mongo_client = pymongo.MongoClient(host='192.168.0.109', port=27017)
        self.collection = self.mongo_client.yikuman.article

    def close_spider(self, spider):
        self.mongo_client.close()

    def process_item(self, item, spider):
        m = self.collection.update({'url': item['url']}, dict(item), upsert=True)
        print(m)
        return item

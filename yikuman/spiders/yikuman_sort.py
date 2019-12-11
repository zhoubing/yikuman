import pymongo

mongo_client = pymongo.MongoClient(host='192.168.0.111', port=27017)
collection = mongo_client.test.article

m = collection.update_one({'name': "123"}, {'$set': {"name": "123"}}, upsert=True)
#
# for title in collection.distinct('title'):
#     count = collection.count({"title": title})
#     if count > 1:
#         for i in range(1, count):
#             collection.remove({"title": title})

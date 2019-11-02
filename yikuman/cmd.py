from scrapy import cmdline

cmdline.execute('scrapy runspider spiders/yikuman_list.py -s JOBDIR=crawls/spider-1 -L WARNING'.split())

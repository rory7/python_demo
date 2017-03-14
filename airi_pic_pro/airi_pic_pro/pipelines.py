# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.exceptions import DropItem


class AiriPicProPipeline(object):
    def get_media_requests(self, item, info):
        for img_url in item['airi_img_url']:
            yield Request(img_url)

    def item_completed(self, results, item, info):
        img_paths = [x['path'] for ok, x in results if ok]
        if not img_paths:
            raise DropItem("图片没下载好 %s" % img_paths)

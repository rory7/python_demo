# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class DoubanNewMoviePipeline(object):
    def __init__(self):
        self.file = codecs.open('douban_new_move.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        # TODO 需要完成以下内容
        line = 'the new mv list:' + "\n"

        for i in range(len(item['mv_star'])):
            mv_name = {'mv_name': str(item['mv_name'][i]).replace(' ', '')}
            mv_star = {'mv_star': str(item['mv_star'][i])}
            mv_url = {'mv_url': str(item['mv_url'][i])}
            line = line + json.dumps(mv_name, ensure_ascii=False)
            line = line + json.dumps(mv_star, ensure_ascii=False)
            line = line + json.dumps(mv_url, ensure_ascii=False) + "\n"

            self.file.write(line)

    def close_spider(self, spider):
        self.file.close()

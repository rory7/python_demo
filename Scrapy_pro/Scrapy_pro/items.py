# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanNewMovieItem(scrapy.Item):
    # define the fields for your item here like:
    mv_name = scrapy.Field()
    mv_star = scrapy.Field()
    mv_url = scrapy.Field()

# coding=utf-8
from scrapy import Selector
from scrapy.spider import Spider

from Scrapy_pro.Scrapy_pro.items import DoubanNewMovieItem


class DoubanNewMvSpider(Spider):
    name = "douban_new_mv_spider"
    start_urls = [
        'http://movie.douban.com/chart'
    ]

    def parse(self, response):
        sel = Selector(response)

        mv_name = sel.xpath("//div[@class='p12']/a/text()").extract()
        mv_url = sel.xpath("//div[@class='p12']/a/text()").extract()
        mv_star = sel.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()").extract()

        item = DoubanNewMovieItem()

        item['mv_name'] = [n.encode('utf-8') for n in mv_name]
        item['mv_star'] = [n for n in mv_star]
        item['mv_url'] = [n for n in mv_url]

        yield item

        print mv_name, mv_star, mv_url

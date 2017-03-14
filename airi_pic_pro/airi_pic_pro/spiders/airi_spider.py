from scrapy.spider import Spider
from scrapy.selector import Selector


class AiriPicSpider(Spider):
    name = "airi_pic_spider"

    start_urls = [
        'http://tieba.baidu.com/p/4023230951'
    ]

    def parse(self, response):
        sel = Selector(response)

        img_url = sel.xpath("//div[@id='post_content_75283192143']/img[@class='BDG_Image']/@src").extract()

        print 'the urls:/n'
        print img_url
        print "/n"

        item = AiriPicSpider()
        item['airi_img_url'] = img_url

        yield item

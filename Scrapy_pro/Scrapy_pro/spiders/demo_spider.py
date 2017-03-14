# # coding=utf-8
# from  scrapy.spiders import Spider
# from  scrapy.selector import Selector
#
#
# class DemoSpider(Spider):
#     name = "demo"
#     allowed_demains = ["demo,org"]
#     start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/"]
#
#     def parse(self, response):
#         sel = Selector(response)
#         sites = sel.xpath('//ul[@class="directory-url"]/li')
#         itms = []
#         for site in sites:
#             itm = DemoSpider()
#             itm['title'] = site.xpath('a/text()').extract()
#             itm['link'] = site.xpath('a/@href').extract()
#             itm['desc'] = site.xpath('text()').extract()
#             itms.append(itm)
#         return itms
#
#
# '''
# sel.xpath('//title')
# 备注：简单的罗列一下有用的xpath路径表达式：
# 表达式	描述
# nodename	选取此节点的所有子节点。
# /	从根节点选取。
# //	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
# .	选取当前节点。
# ..	选取当前节点的父节点。
# @	选取属性。
# '''

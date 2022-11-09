# import scrapy


# class CpSpider(scrapy.Spider):
#     name = 'cp'
#     allowed_domains = ['christianpost.com']
#     start_urls = ['http://christianpost.com/']

#     def parse(self, response):
#         pass
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
 
class article(Item):
    title = Field()
    content=Field()
    url = Field()
    date=Field()
class CpSpider(CrawlSpider):
    custom_settings = {
    'FEED_EXPORT_ENCODING': 'utf-8',
    'FEED_FORMAT': 'csv',
    'FEED_URI': '%(name)s.csv', # %(name)s 会被替换成爬虫的名字，还可以使用%(time)s，记录文件的时间
    # 'FEED_EXPORT_FIELDS': ['text','author']
    # 'LOG_FILE':'%(name)s.log'    
      'CLOSESPIDER_PAGECOUNT': 100

}
    name = "cp"
 
    start_urls = ['https://www.christianpost.com/']
 
    download_delay = 2
 
    rules = (
        Rule( LinkExtractor(allow=r'/news/' ), follow=True, callback="parse_elink"),
        Rule(LinkExtractor(allow=(r'/voices/')),follow=True, callback='parse_elink', )

    )
 
    def parse_elink(self, response):
        sel = Selector(response)
        item = ItemLoader(article(), sel)
 
        item.add_xpath('title', '//h1[@class="article-title"]/text()')
        item.add_xpath('url', '//div[@id="contingut"]/a/@href')
 
        yield item.load_item()
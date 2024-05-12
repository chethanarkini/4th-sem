import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class my(CrawlSpider):
    name='program3'
    allowed_domains=['google.com']
    start_urls=['https://www.google.com/']
    rules=( 
        Rule(LinkExtractor(),callback='parse_page',follow=True),
    )
    def parse_page(self,response):
        title=response.css('title::text').getall()
        paragraphs=response.css('p::text').getall()[:2]
        print("title",title)
        print("paragraphs")
        for para in paragraphs:
            print(para)

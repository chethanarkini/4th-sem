import scrapy
class MySpider(scrapy.Spider):
    name='program1'
    def start_requests(self):
        urls=['https://www.google.com/','https://openweathermap.org/api']
        return [scrapy.Request(url=url,callback=self.parse) 
               for url in urls]
    def parse(self,response):
        url=response.url
        title=response.css('h1::text').getall()
        print("Title {}".format(title))    

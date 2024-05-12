import scrapy
class myclass (scrapy.Spider):
    name='program2'
    start_urls=['https://www.google.com/']
    def parese(self,response):
        images=response.css('img::attr(src)').getall()
        paragraphs=response.css('p::text').getall()

        with open('images.txt','w') as file:
            for img in images:
                file.write(img+'\n')
        with open('paragraphs.txt','w') as file:
            for para in paragraphs:
                file.write(para+'\n')       
import scrapy
import bs4


class AirSpider(scrapy.Spider):
    name = 'air'
    allowed_domains = ['https://www.chinatimes.com/']
    start_urls = ['https://www.chinatimes.com/Search/%E7%A9%BA%E6%B1%A1?chdtv']

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text,'lxml')
        titles=soup.find_all('p',{'class':'intro'})
        for i in titles:    
            print(i.text)

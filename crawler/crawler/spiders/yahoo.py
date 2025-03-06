import bs4
import scrapy


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['tw.yahoo.com']
    start_urls = ['http://tw.yahoo.com/']

    def parse(self, response):
        objSoup= bs4.BeautifulSoup(response.text,'lxml')
        dataTag=objSoup.select('#panel0-content')
        # print('串列長度',len(dataTag))
        headline_news=dataTag[0].find_all('a')
        for h in headline_news:
            news={
                'news_info':h.text,
                'links_info':h.get('herf')
            }
            yield news


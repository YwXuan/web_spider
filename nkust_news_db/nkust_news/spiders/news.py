import scrapy
import time
import random


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.nkust.edu.tw']
    start_urls = ['https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw']

    def parse(self, response):
        for i in range(10):
            time.sleep(random.randint(1, 3))
            url = "https://www.nkust.edu.tw/p/403-1000-1363-" + \
                str(i)+".php?Lang=zh-tw"
            yield scrapy.Request(url, callback=self.parse_info)

    def parse_info(self, response):

        titles = response.css("div.d-txt div.mtitle a::attr(title)").extract()
        abstracts = response.css(
            "div.d-txt div.mdetail div.meditor p::text ").extract()
        dates = response.css("div.d-txt div.mtitle i::text").extract()

        abstracts_index = 0

        news_abstracts = []

        for index in range(0, len(titles)):
            # print("標題:", titles[index])

            text_abstract = ""
            if abstracts[abstracts_index][-3:] != "...":
                # print("摘要:", abstracts[abstracts_index])
                text_abstract = abstracts[abstracts_index] + "\n"
                abstracts_index = abstracts_index + 1

            if abstracts[abstracts_index][-3:] == "...":
                # print("摘要:", abstracts[abstracts_index])
                text_abstract = text_abstract + \
                    abstracts[abstracts_index] + "\n"
                abstracts_index = abstracts_index + 1

            news_abstracts.append(text_abstract)
            # print("\n")

        for info in zip(titles, news_abstracts, dates):
            print("標題:", info[0]),
            print("摘要:", info[1]),
            print("日期:", info[2]),
            news_item = {
                "title": info[0],
                "abstract": info[1],
                "date": info[2]
            }
            yield news_item

        # for index in range(0, len(titles)):
        #     print("標題:", titles[index])
        #     print("摘要1:", abstracts[index*2])
        #     print("摘要2:", abstracts[index*2+1])

import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.nkust.edu.tw']
    start_urls = ['https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw']

    def parse(self, response):

        titles = response.css("div.d-txt div.mtitle a::attr(title)").extract()
        abstracts = response.css(
            "div.d-txt div.mdetail div.meditor p::text ").extract()

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

        for info in zip(titles, news_abstracts):
            print("標題:", info[0]),
            print("摘要:", info[1]),
            news_item = {
                "標題": info[0],
                "摘要": info[1]
            }
            yield news_item

        # for index in range(0, len(titles)):
        #     print("標題:", titles[index])
        #     print("摘要1:", abstracts[index*2])
        #     print("摘要2:", abstracts[index*2+1])

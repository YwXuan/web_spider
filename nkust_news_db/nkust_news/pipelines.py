# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class NkustNewsPipeline:

    def open_spider(self, spider):
        self.conn = sqlite3.connect("news.db")
        self.cur = self.conn.cursor()
        sql = '''Create table news(
                title TEXT,
                abstract TEXT,
                date TEXT)'''
        self.cur.execute(sql)

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        title = item['title']
        abstract = item['abstract']
        date = item['date']
        x = (title, abstract, date)
        sql = '''insert into news values(?,?,?)'''
        self.conn.execute(sql, x)
        return item

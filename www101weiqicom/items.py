# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Www101WeiqicomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    level = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    

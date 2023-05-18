import scrapy


class JobItem(scrapy.Item):
    job = scrapy.Field()
    company = scrapy.Field()
    type = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()

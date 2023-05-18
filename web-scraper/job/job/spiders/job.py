import scrapy
from job.items import JobItem
import datetime

class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["seek.co.nz"]
    start_urls = [
        "https://www.seek.co.nz/jobs-in-information-communication-technology/"]
    custom_settings = {"FEEDS": {"data.csv": {"format": "csv"}}}

    def parse(self, response):
        links = response.xpath(
            '//a[@data-automation="jobTitle"]/@href').getall()
        
        for l in links:
            jobLink = response.urljoin(l)
            yield scrapy.Request(jobLink, callback=self.parse_item)

        next_page = response.xpath('//a[@title="Next"]/@href').extract_first()
        url = response.urljoin(next_page)
        yield scrapy.Request(url, callback=self.parse)

    def parse_item(self, response):
        item = JobItem()
        
        item['job'] = response.xpath(
            '//h1[@data-automation="job-detail-title"]/text()').extract()

        item['company'] = response.xpath(
            '//span[@data-automation="advertiser-name"]/text()').extract()

        item['location'] = response.xpath(
            '//div[@class="_1wkzzau0 a1msqi5a a1msqiga"]//div//div//span/text()').extract_first()

        item['type'] = response.xpath(
            '//span[@data-automation="job-detail-work-type"]/text()').extract()

        item['description'] = response.xpath(
            '//div[@data-automation="jobAdDetails"]/div//text()').extract()
        
        yield item

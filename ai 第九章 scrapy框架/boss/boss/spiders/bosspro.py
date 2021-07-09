import scrapy
from boss.items import BossItem
import time

class BossproSpider(scrapy.Spider):
    name = 'bosspro'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python']

    new_url = 'https://www.zhipin.com/job_detail/?query=python&page=%d'
    page_num = 2

    def detail_parse(self,response):

        item = response.meta['item']

        job_detail = response.xpath('//*[@id="main"]/div[2]/div/div[2]/div[2]/div[1]/div/text()').extract()
        job_detail = ''.join(job_detail)
        item['job_detail'] = job_detail

        yield item

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        print(li_list)
        for li in li_list:

            job_name = li.xpath('.//div[@class="job-title“]/span[1]/a/text()').extract_first()
            print(job_name)
            job_href = 'https://www.zhipin.com'+li.xpath('//div[@class="job-title“]/span[1]/a/@href').extract_first()
            print(job_href)
            item = BossItem()
            item['job_name'] = job_name
            yield scrapy.Request(job_href,callback= self.detail_parse,meta={'item':item})

        if self.page_num <=3:
            url = format(self.new_url%self.page_num)
            self.page_num += 1

            yield scrapy.Request(url,callback=self.parse)

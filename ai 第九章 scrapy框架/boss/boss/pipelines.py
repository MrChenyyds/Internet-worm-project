# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



class BossPipeline:
    def process_item(self, item, spider):
        print(item)
        return item

    # fp = None
    #
    # def open_spider(self, spider):
    #     print('开始爬虫。。。。。。')
    #     self.fp = open('./boss_data.txt','w',encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #
    #     job_name = item['job_name']
    #     job_detail = item['job_detail']
    #
    #     self.fp.write(job_name+'\n'+job_detail+'\n')
    #
    #     print(item)
    #     return item
    #
    # def close_spider(self, spider):
    #     print('爬虫结束！！！！')
    #     self.fp.close()
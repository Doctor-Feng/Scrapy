import scrapy
from yamaxun.items import YamaxunItem
class MySpider(scrapy.spiders.BaseSpider):
    name = "spider"
    start_urls = ["https://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E7%95%85%E9%94%80%E4%B9%A6&rh=i%3Aaps%2Ck%3A%E7%95%85%E9%94%80%E4%B9%A6"]

    def parse(self,response):
        for sel in response.xpath('//html'):
            item = YamaxunItem()
            #item['name'] = sel.xpath('//div[@class="a-row a-spacing-none"]/a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/h2[@class="a-size-base s-inline  s-access-title a-text-normal"]/text()')[0].extract()
            item['name'] = sel.xpath('//div[@class="a-row a-spacing-none"]/a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/h2/text()').extract()

            yield item

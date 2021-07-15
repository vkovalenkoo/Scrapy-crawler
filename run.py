import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from Top.spiders.spidertwich import ViewerSpider

process = CrawlerProcess(get_project_settings())

process.crawl(ViewerSpider)
process.start()  # the script will block here until the crawling is finished
# input('Press any to continue')
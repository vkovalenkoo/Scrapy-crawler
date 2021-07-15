BOT_NAME = 'Top'

SPIDER_MODULES = ['Top.spiders']
NEWSPIDER_MODULE = 'Top.spiders'

ROBOTSTXT_OBEY = True # Obey robots.txt rules
USER_AGENT = 'diligent spider' #set a random user_agent for take access to the site

CONCURRENT_REQUESTS_PER_DOMAIN = 1

ITEM_PIPELINES = {
   'Top.pipelines.CsvPipeline': 300,
}
CLOSESPIDER_ITEMCOUNT = 100    #Setting the scan limit (change it for take necessary data count)
DOWNLOAD_DELAY = 3             #Set the speed limit (3 is optimal value. You can try to  change to smaller number, but bot will scip some links)

import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor

class ViewerSpider(scrapy.Spider):
    name = 'Billy'
    start_urls = ['https://twitchtracker.com/channels/viewership']                                    #starting url

    def parse(self, response):
        stats_cells = response.xpath('//table[@id="channels"]/tbody/tr')                              #accept a table with data for further scraping
        for statistics in stats_cells:                                                                #iterate over the table using a loop and xpath
            channel_url = statistics.xpath('./td[2]/a/@href').extract()                               #getting a fragment of the streamer link
            if channel_url:                                                                           #condition for the fix bag and crush
                channel_url = 'https://twitchtracker.com' + channel_url[0] + '/statistics'            #make correct URL
                yield Request(channel_url, callback=self.parse_statistics)                            #set a new url(channels_url) and go to getting statistics in other def

        next_url = response.css('.pagination a[rel="next"]::attr(href)').get()                        #get link for the next page.Here the link looks fine,so we woun't have to collect our Frankenstein
        yield Request(next_url, callback=self.parse)                                                  #set a new url(to the next page) and retur to our function

    def parse_statistics(self, response):                                           #pass self to our function for get url and response for get data from the site
        item = {}                                                                   #all data will be in one dictionary
        item['name_channel'] = response.css("div#app-title::text").get().strip()    # the channel name is searched throughout the site, so use response.css. there is strip in the and that delete unnecessary space
        item['name_url'] = response.url                                             # response.url is current link

        stats_cells = response.css('div.pg-controls .pge')                          # accept the path to the data location
        for statistics in stats_cells:                                              # and go through each
            heading = statistics.css("div.pge-t::text").get()                       # get the heading in accepted way,so use  statistics.css
            item[heading] = statistics.css("div.pge-v span::text").get().strip()    # and write information in item with our heading's name
        yield item                                                                  # return our dictionary with data for save in file

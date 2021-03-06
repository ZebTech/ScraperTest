from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector


class MininovaSpider(CrawlSpider):

    name = 'mininova'
    allowed_domains = ['tooski.ch']
    start_urls = ['http://www.tooski.ch']
    rules = [Rule(SgmlLinkExtractor(allow=['/comment.php?id=\d+']), 'parse_torrent')]

    def parse_torrent(self, response):
        sel = Selector(response)
        torrent = TorrentItem()
        torrent['url'] = response.url
        torrent['name'] = sel.xpath("//h1/text()").extract()
        # torrent['description'] = sel.xpath(
        #     "//div[@id='description']").extract()
        # torrent['size'] = sel.xpath(
        #     "//div[@id='info-left']/p[2]/text()[2]").extract()
        return torrent

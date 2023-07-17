```python
import scrapy
from web_scraper.items import RedditItem

class RedditSpider(scrapy.Spider):
    name = "reddit"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://www.reddit.com/"]

    def parse(self, response):
        for post in response.css('div.thing'):
            item = RedditItem()
            item['title'] = post.css('p.title a.title::text').extract_first()
            item['url'] = post.css('p.title a.title::attr(href)').extract_first()
            item['upvotes'] = post.css('div.score.unvoted::attr(title)').extract_first()
            yield item

        next_page = response.css('span.next-button a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```
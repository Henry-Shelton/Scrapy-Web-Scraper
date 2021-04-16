import scrapy

class PostsSpider(scrapy.Spider):

    name = "posts"

    start_urls = [
        'https://www.better.org.uk/leisure-centre/london/camden/kentish-town-sports-centre/',
        'https://www.better.org.uk/leisure-centre/london/camden/oasis-sports-centre/',
        'https://www.better.org.uk/leisure-centre/london/camden/pancras-square/',
        'https://www.better.org.uk/leisure-centre/london/camden/swiss-cottage-leisure-centre/',
        'https://www.better.org.uk/leisure-centre/london/camden/talacre-community-sports-centre/',
        'https://www.better.org.uk/leisure-centre/london/bexley/better-gym-bexley/',
        'https://www.better.org.uk/leisure-centre/london/bexley/bexleyheath/',
        'https://www.better.org.uk/leisure-centre/london/bexley/better-gym-sidcup/',
        'https://www.better.org.uk/leisure-centre/london/croydon/ashburton-hall-park/',
        'https://www.better.org.uk/leisure-centre/london/croydon/croydonparks/',
        'https://www.better.org.uk/leisure-centre/london/croydon/croydon-sports-arena/',
        'https://www.better.org.uk/leisure-centre/london/croydon/monks-hill-sport-centre/',
        'https://www.better.org.uk/leisure-centre/london/croydon/new-addington-leisure-centre/',
        'https://www.better.org.uk/leisure-centre/london/croydon/purley-leisure-centre/',
        'https://www.better.org.uk/leisure-centre/london/croydon/south-norwood-leisure-centre/'
    ]

    def parse(self, response):
        for post in response.xpath('/html/body/main'):
            yield {
                'name': response.xpath('/html/body/main/div[2]/div/section/header/h1/text()').get(),
                'price': response.xpath('/html/body/main/section/ul/li/div[1]/div[2]/text()').get(),
                'postcode': response.xpath('/html/body/main/div[2]/div/section/ul/li[1]/a/span/text()[4]').get(),
                'phone':  response.xpath('/html/body/main/section/div[5]/div/div[3]/div/ul/li[1]/a/text()').get()
            }

#ctrl + / tp comment out

# 1) start virtual env by activating (venv) = cd webscraper/venv/scripts/activate
# 2) to start a website to extract info = scrapy shell 'URL'
# 3) use commands here (can use [0] for specific selection) = response.css('').get() + response.xpath('').extract() ect (check docs)
# 4) code in parse script and file print destination
# 5) any other scrapy manipulations now
# 6) to run the script = scrapy crawl posts -o posts.json OR .csv

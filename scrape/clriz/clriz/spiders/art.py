# -*- coding: utf-8 -*-
# pdanshov feb 13 2018
'''
author: Peter Danshov
date: April 12 2018
version: 1.1.2

version 1.1.2
    Apr 12th 2018
    added variable & loop for counter, for each entry everytime the script runs
version 1.1.1
    Feb 21st 2018
    added variable for search term, and replaced url's with variable
version 1.1
    Feb 19th 2018
    added michigan area, and additional states
version 1.0
    feb 13th 2018
     source: http://python.gotrained.com/scrapy-tutorial-web-scraping-craigslist/
     run in terminal: scrapy crawl art
     run for csv export: scapy crawl art -o art_x.csv
''' and None

import scrapy
import datetime


class ArtSpider(scrapy.Spider):
    name = "art"
    allowed_domains = ["craigslist.org"]
    searchterm = 'rizzi'
    start_urls = ['https://newyork.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=59&nearbyArea=248&nearbyArea=451&nearbyArea=349&nearbyArea=193&nearbyArea=281&nearbyArea=166&nearbyArea=44&nearbyArea=249&nearbyArea=561&nearbyArea=279&nearbyArea=167&nearbyArea=250&nearbyArea=168&nearbyArea=170&nearbyArea=354&nearbyArea=684&nearbyArea=17&nearbyArea=356&nearbyArea=278&nearbyArea=276&nearbyArea=286&nearbyArea=173&nearbyArea=357','https://losangeles.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=63&nearbyArea=43&nearbyArea=709&nearbyArea=455&nearbyArea=104&nearbyArea=26&nearbyArea=285&nearbyArea=96&nearbyArea=565&nearbyArea=102&nearbyArea=103&nearbyArea=209&nearbyArea=8&nearbyArea=191&nearbyArea=62&nearbyArea=710&nearbyArea=181&nearbyArea=208&nearbyArea=346&nearbyArea=370','https://sfbay.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=63&nearbyArea=187&nearbyArea=43&nearbyArea=373&nearbyArea=709&nearbyArea=189&nearbyArea=454&nearbyArea=285&nearbyArea=96&nearbyArea=102&nearbyArea=188&nearbyArea=92&nearbyArea=12&nearbyArea=191&nearbyArea=62&nearbyArea=710&nearbyArea=708&nearbyArea=97&nearbyArea=707&nearbyArea=208&nearbyArea=346&nearbyArea=456','https://miami.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=238&nearbyArea=330&nearbyArea=125&nearbyArea=219&nearbyArea=639&nearbyArea=376&nearbyArea=333&nearbyArea=39&nearbyArea=237&nearbyArea=331&nearbyArea=557&nearbyArea=37&nearbyArea=332','https://annarbor.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=251&nearbyArea=700&nearbyArea=628&nearbyArea=434&nearbyArea=484&nearbyArea=27&nearbyArea=42&nearbyArea=22&nearbyArea=259&nearbyArea=226&nearbyArea=129&nearbyArea=630&nearbyArea=426&nearbyArea=261&nearbyArea=212&nearbyArea=437&nearbyArea=234&nearbyArea=436&nearbyArea=629&nearbyArea=554&nearbyArea=309&nearbyArea=555&nearbyArea=260&nearbyArea=573&nearbyArea=486&nearbyArea=228&nearbyArea=572&nearbyArea=627&nearbyArea=204&nearbyArea=235','https://chicago.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=243&nearbyArea=628&nearbyArea=344&nearbyArea=190&nearbyArea=569&nearbyArea=362&nearbyArea=226&nearbyArea=129&nearbyArea=630&nearbyArea=45&nearbyArea=426&nearbyArea=553&nearbyArea=261&nearbyArea=552&nearbyArea=672&nearbyArea=698&nearbyArea=360&nearbyArea=212&nearbyArea=165&nearbyArea=699&nearbyArea=47&nearbyArea=361&nearbyArea=554&nearbyArea=224&nearbyArea=307&nearbyArea=223&nearbyArea=571&nearbyArea=228&nearbyArea=572&nearbyArea=348','https://seattle.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=217&nearbyArea=233&nearbyArea=473&nearbyArea=350&nearbyArea=322&nearbyArea=94&nearbyArea=471&nearbyArea=381&nearbyArea=380&nearbyArea=324&nearbyArea=654&nearbyArea=655&nearbyArea=382&nearbyArea=466&nearbyArea=321&nearbyArea=9&nearbyArea=368&nearbyArea=459&nearbyArea=232&nearbyArea=461&nearbyArea=95&nearbyArea=622&nearbyArea=16&nearbyArea=177&nearbyArea=325&nearbyArea=472&nearbyArea=246','https://dallas.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=364&nearbyArea=15&nearbyArea=264&nearbyArea=644&nearbyArea=326&nearbyArea=645&nearbyArea=293&nearbyArea=358&nearbyArea=470&nearbyArea=23&nearbyArea=327&nearbyArea=284&nearbyArea=422&nearbyArea=100&nearbyArea=267&nearbyArea=563&nearbyArea=650&nearbyArea=54&nearbyArea=646&nearbyArea=53&nearbyArea=449&nearbyArea=206&nearbyArea=433&nearbyArea=359&nearbyArea=649&nearbyArea=70&nearbyArea=308&nearbyArea=564&nearbyArea=270&nearbyArea=365','https://washingtondc.craigslist.org/search/sss?query='+str(searchterm)+'&sort=rel&searchNearby=2&nearbyArea=355&nearbyArea=460&nearbyArea=34&nearbyArea=349&nearbyArea=290&nearbyArea=705&nearbyArea=193&nearbyArea=444&nearbyArea=328&nearbyArea=633&nearbyArea=457&nearbyArea=166&nearbyArea=447&nearbyArea=561&nearbyArea=279&nearbyArea=167&nearbyArea=366&nearbyArea=440&nearbyArea=48&nearbyArea=17&nearbyArea=356&nearbyArea=278&nearbyArea=60&nearbyArea=286&nearbyArea=556&nearbyArea=277&nearbyArea=329&nearbyArea=463&nearbyArea=711&nearbyArea=357']

    '''
    washingtondc + surrounding area
    dallas + surrounding area
    seattle + surrounding area
    chicago + surrounding area
    annarbor + surrounding michigan area
    nyc+nearby= albany, binghampton, catskills, centralNJ, delaware, easternCT, harrisburgPA, hartfordCT, hudsonValleyNY, JerseyShore, lancasterPA, lehighvalley, LongIsland, NewHavenCT, NorthJersey, NorthwestCT, OneontaNY, Philadelphia, Poconos, ReadingPA, Scranton/wilkesbarre, SouthJersey, WesternMA, YorkPA
        CL codes(same order as above):
    LA+nearby= bakersfieldCA, fresno/madera, hanford-corcoran, imperialCounty, inlandEmpireCA, lasVegas, mercedCA, modestoCA, mohaveCounty, montereyBay, orangeCountyCA, palmSpringsCA, sanDiego, sanLuisObispo, santaBarbara, santaMariaCA, tijuanaMX, venturaCounty, visalia-tulare, yumaAZ
        CL codes:
    SFBay+nearby= bakersfieldCA, chicoCA, fresno/madera, goldCountry, hanford-corcoran, humboldtCounty, mendocinoCounty, mercedCA, modestoCA, montereyBay, reddingCA, reno/tahoe, sacramento, sanLuisObispo, santaBarbara, santaMariaCA, siskiyouCounty, stocktonCA, susanvilleCA, venturaCounty, visalia-tulare, yuba-sutterCA
        CL codes:
    Miami+nearby= daytonaBch, flkeys, ftmyers/swfl, gainesville, heartlandfl, lakeland, ocala, orlando, sarasota-bradenton, spacecoast, staugustine, tampabay, treasurecoast
        CL codes: dab, key, fmy, gnv, cfl, lal, oca, orl, srq, mlb, ust, tpa, psl
    ''' and None



    def parse(self, response):

### extract just title
###        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

        '''
        -|extract the a, class="", text between a
        -|<ahref="https://newyork.craigslist.org/mnh/tix/d/turandot-met-opera-discounted/6493464298.html" data-id="6493464298"
            class="result-title hdrlnk">
                Turandot - Met Opera - Discounted Tickets Available</a>
        -|print(response) - will output a code+url indicating a status of attempt to connect to a website
        -|print(response.body) - will output the page source code
        -|when using xpath to extract html nodes, you should directly use reponse.xpath()
        ''' and None

### basic print titles from title extract above
##        print(titles)


### extract wrapper & sort-select elements within
        art = response.xpath('//p[@class="result-info"]')

        #we started the XPath expression of “jobs” by // meaning it starts from <html> until this <p> whose class name is  “result-info”.

        today = datetime.datetime.now()

        counter = 1

        for piece in art:
            title = piece.xpath('a/text()').extract_first()
            address = piece.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
            relative_url = piece.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)

            count = str(counter)

            yield{'No.':count, 'Scrape':today, 'URL':absolute_url, 'Title':title, 'Address':address}

            counter += 1

            '''
            -|you do not use “response” (which you already used to extract the wrapper). Instead, you use the wrapper selector
            we started the XPath expression of “title” without any slashes, because it complements or depends on the XPath expression of the job wrapper.
            -|If you rather want to use slashes, you will have to precede it with a dot to refer to the current node as follows:
            title = piece.xpath('.//a/text()').extract_first()
            -|As we explained in the first part of this Scrapy tutorial, a refers to the first <a> tag inside the <p> tag, and text() refers to the text inside the <a> tag which is the job title.
            -|Here, we are using extract_first() because in each iteration of the loop, we are in a wrapper with only one job.
            -|To extract the job address, you refer to the <span> tag whose class name is “result-meta” and then the <span> tag whose class name is “result-hood” and then the text() in it. The address is between brackets like (Brooklyn); so if you want to delete them, you can use string slicing [2:-1]. However, this string slicing will not work if there is no address (which is the case for some jobs) because the value will be None which is not a string! So you have to add empty quotes inside extract_first("") which means if there is no result, the result is “”.
            ''' and None #to invalidate the docstring, e.g: make the context a comment (also if False: ''' ''')






###        pass

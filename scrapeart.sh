#!/bin/bash

#pdanshov feb 13 2018

cd ./scrape/clriz/clriz/spiders/
scrapy crawl art -o art_.csv

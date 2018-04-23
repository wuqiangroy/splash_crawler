# -*- coding: utf-8 -*-

# Scrapy settings for splash_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'splash_crawler'

SPIDER_MODULES = ['splash_crawler.spiders']
NEWSPIDER_MODULE = 'splash_crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'splash_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# splash url
# do not use localhost, use your ip
SPLASH_URL = "182.138.169.40"

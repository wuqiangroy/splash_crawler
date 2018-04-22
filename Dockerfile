FROM python3:3.6.3
ADD splash_crawler /splash_crawler
WORKDIR /splash_crawler

RUN apt-get install supervisor &&
    pip3 install -i https://pypi.douban.com/simple -r requirements.txt
RUN mkdir -p /var/www

ADD supervisord.conf /var/www/supervisord.conf
CMD ["/usr/bin/supervisord", "-c", "/var/www/supervisord.conf"]

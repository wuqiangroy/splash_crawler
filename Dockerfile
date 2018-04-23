FROM python:3.6.5
ADD . /splash_crawler
WORKDIR /splash_crawler

RUN apt-get update && apt-get install -y supervisor && \
    pip install -i https://pypi.douban.com/simple -r requirements.txt
RUN mkdir -p /var/log/supervisor
EXPOSE 5000
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

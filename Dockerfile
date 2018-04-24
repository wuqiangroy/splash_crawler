FROM python:3.6.5
ENV PATH /usr/local/bin:$PATH
ADD . /splash_crawler
WORKDIR /splash_crawler

RUN apt-get update && \
    apt-get install -y supervisor && \
    pip install -r requirements.txt -i https://pypi.douban.com/simple
RUN mkdir -p /var/log/supervisor

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 5000
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]

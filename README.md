## Splash-Crawler
docker 封装的含有 web ui 的爬虫管理工具

### ENV
the project environment
- python 3.6.3
- scrapy 1.5.0
- scrapyd 2.18
- spiderkeeper 1.2.0
- Splash lates

### Deploy
#### step 1
scrapyd-deploy --build-egg output.egg
#### step 2
execute command:
- `scrapyd`
- `spiderkeeper`
#### step 3
visit `localhost:5000`
username and password is `admin`
create a new project and choose output.egg file from step 1 we created
#### step 4
shut down scrapyd
shut down spiderkeeper
the:
`docker-compose up`

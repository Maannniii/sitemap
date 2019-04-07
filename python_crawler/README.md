### Prerequisites:
1. [python3](https://realpython.com/installing-python "Installing python3")
2. [pip3](https://pip.pypa.io/en/stable/installing/ "Installing pip3")
3. [MySQL 5.7.8+](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/ "Installing MySQL")

This project assumes that you already have the above mentioned prerequisites installed.

### Setup
1. Install the required python libraries by running `pip install -r requirements.txt` found under `sitemap_crawler`.
2. Update the database configurations found at `sitemap_crawler/sitemap_crawler/settings.py`

### Running
* Change directory to `sitemap_crawler`
* To view list of available spiders run `scrapy list`
* To run a spider use `scrapy crawl [spider_name]`. 
* To crawl and store the data as json/xml file run `scrapy crawl [spider_name] -o filename.[json|xml]`. This stores data to Database and Respective file as well.

## Note:  
**1. The crawler will truncate the data stored in the database each time. comment the lines 18,19,20 at `sitemap_crawler/pipelines.py` to disable it.**

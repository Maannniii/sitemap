# Sitemap Generator
Sample project for crawling site and Generating sitmap.
The project uses Python and Scrapy for crawing websites and Java for exposing the crawled data as REST Api.

### Prerequisites:
1. [python3](https://realpython.com/installing-python "Installing python3")
2. [pip3](https://pip.pypa.io/en/stable/installing/ "Installing pip3")
3. [MySQL 5.7.8+](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/ "Installing MySQL")
4. [Java jdk 1.8+](https://www.java.com/en/download/help/download_options.xml "Java installation")
5. [Apache maven 3+](https://maven.apache.org/install.html "Maven Installation")

Install the above mentioned Prerequisites before starting the project.

Once done create a table having following columns

| Name | Type | Constraint |
| ------ | ------ | ------ |
| id | int(11) | NOT NULL, AUTO_INCREMENT, PRIMARY KEY |
| url | varchar(1000) | NOT NULL |
| external_urls | JSON | NOT NULL |
| static_urls | JSON | NOT NULL |
| urls | JSON | NOT NULL |

Refer `MySQL / table.sql` for syntax.

Please find **README.md** inside the project directories for more specific instructions.

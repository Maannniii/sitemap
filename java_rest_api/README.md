Spring boot project to expose crawled Sitemap Data.  
This project reads and exposes stored data from MySQL database as JSON response.

### Prerequisites:
1. [Java jdk 1.8+](https://www.java.com/en/download/help/download_options.xml "Java installation")
2. [Apache maven 3+](https://maven.apache.org/install.html "Maven Installation")

This project assumes that you already have the above mentioned prerequisites installed and have ran the python crawler already.

### Running
* Change directory to `rest`
* Update database properties at `rest/src/main/resources/application.properties`.
* Compile and create jar by running `mvn clean package`
* Once done run the jar under target directorty as `java -jar jarname.jar`. Here `java -jar rest-0.0.1.jar`
* Open your browser and navigate to `http://localhost:8080/sitemap` to get the JSON response.


### Available APIs:
* **`GET /sitemap` or `/sitemap/all`**
* **`GET /sitemap/{id}`**

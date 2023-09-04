[![Docker Repository on Quay](https://quay.io/repository/ticy_y/get_crypto_price/status "Docker Repository on Quay")](https://quay.io/repository/ticy_y/get_crypto_price)
# Automatically Execute Containerized Cryptocurrency Price Crawling Program via Linux Crontab  
## Environment  
- Host: VMware Workstation 17 Player + Ubuntu 22.04  
- Files Description  
- Dockerfile:  
  - Base image: python:3.10-alpine  
  - Timezone set to Taipei  
- docker_build.sh: A bash script used to build the Docker image and start the container. It also defines the directory is mounted into a container.
- get_crypto_price.py: Python web scraping script utilizing pandas, requests, BeautifulSoup  

## Automated Scheduling with Linux Commands
Schedule automatic execution using the following command:  

    crontab -e  

Add the following line to execute the container every 10 minutes:  

    */10 * * * * docker start crypto_ctr

## Using the Docker image
The Docker image could be pulled using the following command: 

    docker pull quay.io/ticy_y/get_crypto_price

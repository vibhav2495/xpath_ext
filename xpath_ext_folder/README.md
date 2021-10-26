## XPATH EXTRACTOR DOCUMENTATION

This project includes a web scraping tool to extract the data mapped to a particular x-path in a website.
A YAML script is being used to give the site details including URL and x-path classname.

Directory stucture
.
├── README.md
├── XPATH_GEN_FOLDER
│   ├── xml_xpath_file_headless.py
├── config
│   └── sites.yaml

`XPATH_GEN_FOLDER`:This folder contains the source code and the configuration files needed to accomplish XPATH data extraction.

`config`:This directory contains the website values for passing the HTML request and obtaining the scraped data included in the YAML based config files.

## Examples

With the help of website URL and x-path class in the YAML file, the python program extracts the website data. One example would be using the "https://www.fecareers.co.uk/job-results?sort=date#" (URL) and job-location (x-path class) to extract all the job locations present in the website.

## Environment requirements

Python 3.6.0 or higher

## Running Xpath Extractor

To start with, have python installed on your local machine and then install the dependencies "requests html" and "YAML" libraries through the "pip install" commands in your python terminal.

To run the program, the following steps should be done:

- Check the "sites.yaml" file and make sure if the data extraction is happening at the right URL and Xpath class name. If not, relevant URL and Xpath class name details needs to be updated.

- Next run the program in any comfortable IDE (example: Visual Studio Code) that supports python and the required data will be extracted in the console.

## Author:

Vibhav Kannan (vibhavk@student.unimelb.edu.au)

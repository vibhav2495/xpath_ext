## XPATH EXTRACTOR DOCUMENTATION

This project includes a web scraping tool to extract the data mapped to a particular x-path in a website.
A YAML file is being used to provide the configuration including URL and x-path classname to the python application.

Directory stucture

```
.
└── src
    ├── config
    │   └── sites.yaml
    ├── README.md
    └── xml_xpath_file_headless.py

```

`src`: This folder contains the source code and the configuration file needed to accomplish XPATH data extraction.

`config`: This directory contains the YAML configuration file which is used to specify the required application parameters such as the URL and the X-path class.

## Examples

The YAML file is the main configuration file containing the website URL that needs to be visited and the relevant x-path class required for the python program to extract the website data. The file contains the following structure:

```
sites:
  - site: "<Enter the Website URL which needs to be visited>"
    x-path: "<The x-path that needs to be extracted from the above url>"
```

The `sites` param is used to denote a list of `site` and the corresponding `x-path` that will be used by the python application to retrieve the relevant information. To include multiple sites, add further entries of `site` and `x-path` and the python application will use these to iterate over the site specific url and x-path.

As an example, if we were to retrieve the x-path `job-location` from the site https://www.fecareers.co.uk/job-results?sort=date#, the configuration params will look like the following:

```
sites:
  - site: "https://www.fecareers.co.uk/job-results?sort=date#"
    x-path: "job-location"
```

To scrape a new website, add a new entry for the `site` and `x-path` in the YAML configuration file.

## Environment requirements

- Python 3.6.0 or higher
- requests_html python package
- yaml python package

## Running Xpath Extractor

To start with, setup your environment with the abovementioned dependencies and execute our python application as follows:

- Enter the details for the website to be scraped in the YAML configuration file (please see example).
- Run the program using an IDE or via a terminal as follows:

```
>> python xml_xpath_file_headless.py
```

## Author:

Vibhav Kannan (vibhavk@student.unimelb.edu.au)

"""Main file for xpath web extraction

This file uses request_html library to connect to a given website in the yaml configuration and 
extract the data pointed by a class in x-path.

Author: Vibhav Kannan <vibhavk@student.unimelb.edu.au>
"""

import requests_html
import yaml

#Reads the website details from /config directory.
site_config = "./config/sites.yaml"
with open(site_config) as config:
  config_list = yaml.load(config, Loader=yaml.FullLoader)

#Reads the site URL and x-path class details in sites list
lista=config_list["sites"]

#On request HTMLSession initiates an internal browser session
session = requests_html.HTMLSession()

"""Loops through and extract the relevant x-path data.
 Keywords used are:
 session.get()- Downloads the source content of the page
 html.xpath() - Looks through and maps the relevant x-path elements in the source.
"""
for i in lista:
  r = session.get(i["site"])
  val= r.html.xpath("//span[contains(@class, '" + i["x-path"] + "')]")
  for item in val:
      print(item.text)
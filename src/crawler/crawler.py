import re
import codecs
import sys
import os
import requests
from selenium import webdriver
from urlparse import urlparse

if os.path.isfile("/etc/requests.txt"):
	file = "/etc/requests.txt"
else:
	if os.path.isfile("~/requests.txt"):
		file = "~/requests.txt"
	else:
		if os.path.isfile("./requests.txt"):
			file = "./requests.txt"
		else:
			raise "no requests.txt specified"
		 

	

with open(file) as f:
    request_list = f.readlines()

f = codecs.open('index.html', mode='w', encoding='utf-8')

for req in request_list:
	result = requests.get(req)
	parsed_uri = urlparse(req)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	page1 = re.sub("src=\"", "src=\"" + domain, result.text)
	page2 = re.sub("href=\"", "href=\"" + domain, result.text)
	f.write(page2)

f.close()

driver = webdriver.Firefox()
driver.get("file://" + os.getcwd() + "/index.html")


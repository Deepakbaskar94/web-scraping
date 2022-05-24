# Import Module
from bs4 import BeautifulSoup
import requests

# Website URL
URL = "https://www.91mobiles.com/mobile-phones"
#URL = 'https://www.geeksforgeeks.org/'

# class list set
class_list = set()

# Page content from Website URL
page = requests.get(URL)

# parse html content
soup = BeautifulSoup(page.content, 'html.parser')

# get all tags
tags = {tag.name for tag in soup.find_all()}

# iterate all tags
for tag in tags:

    # find all element of tag
    for i in soup.find_all(tag):

        # if tag has attribute of class
        if i.has_attr("id"):

            if len(i['id']) != 0:
                class_list.add("".join(i['id']))

printvalue = class_list

printvalue = str(printvalue)
f = open("demofile2.txt", "w")
f.write(printvalue)
f.close()
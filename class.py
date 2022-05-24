

# Import Module
from bs4 import BeautifulSoup
import requests


# Website URL
URL = ("https://www.91mobiles.com/mobile-phones")
# class list set
class_list = set()

# Page content from Website URL
page = requests.get(URL)
from csv import writer
# parse html content
soup = BeautifulSoup(page.content, 'html.parser')

# get all tags
tags = {tag.name for tag in soup.find_all()}

with open('file.csv' , 'w' , newline='' , encoding='utf8')as f:
    thewriter = writer(f)
    header = ['class']
    thewriter.writerow(header)



    # iterate all tags
    for tag in tags:

        # find all element of tag
        for i in soup.find_all(tag):

            # if tag has attribute of class
            if i.has_attr("class"):

                if len(i['class']) != 0:

                    class_list.add(" ".join(i['class']))
                    list1 = list(class_list)

                    #print(type(class_list))
                    for x in list1:
                        autoinfo=[x]
                        thewriter.writerow(autoinfo)


##my_file = open("demofile2.txt", "w")
# reading the file
##data = my_file.write()


# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
##data_into_list = data.replace('\n', ' ').split(".")

# printing the data

##print(data_into_list)
##my_file.close()


#Data collection using BeautifulSoup from a page directly from webpage using get request
# importing the modules

from bs4 import BeautifulSoup
import requests
from csv import writer


list1 = []
list1 = list(list1)
# Fetch the page and create a Beautiful Soup object
page = requests.get(url = "https://www.91mobiles.com/phonefinder.php")

soup = BeautifulSoup(page.content, 'html.parser')
# for tag in soup.find_all('div',{"class":"title"}):
#     print(tag.text)
# for tag in soup.find_all('div', {"class": "price"}):
# 	print(tag.text)

with open('file.csv' , 'w' , newline='' , encoding='utf8')as f:
    thewriter = writer(f)
    #header = ['class']
    #thewriter.writerow(header)

    ###filtering the division which is having class item
    for link in soup.find_all('div', {"class":"filter-grey-bar"}):
        #print(link)
        ###In the filtered division filtering only the h5 tag
        links = link.find('li')
        ###Inside the h5 tag checking a tag is not none if it is none it will pop up an error
        if links is not None:
            #print(links)
        ###Under the h5 tag getting inside the a tag and finding the attribute href is having some data
            for a in links.find_all('a', href=True):
                href1 = a['href']
                title1 = a['title']
                #print(title1)
                #print(href1)
                if href1 is not None and title1 is not None:
                    #print(href1)
                    list1.append(title1)
                    list1.append(href1)
                    #print (list1)
                    #list1 = []
                else:
                    pass
        else:
            pass

        #for price in link.find_all('div', {"class":"price.price_padding"}):
            #list1.append(price)
            #print(price)
        for tag in link.find_all('span',{"class":"price price_padding"}):
            #thewriter.writerow(tag.text)
            list1.append(tag.text)
            #print(list1)
            #list1 = []
            #print(tag.text)

        for details in link.find_all('div', {"class":"filter-grey-bar filter_gray_bar_margin"}):
            #print(details)
            for column in details.find_all('div', {"class":"left specs_li"}):
                #print(column)
                for block in column.find_all('div', {"class":"a filter-list-text"}):
                    #print(block)
                    for value in block.find_all('label', title=True):
                        #href1 = a['href']
                        #title1 = a['title']
                        data = value['title']
                        #print(data)
                        list1.append(data)
            #print(list1)
            thewriter.writerow(list1)
            list1 = []
            
                        #print(href1)
                        # if href1 is not None and title1 is not None:
                        #     #print(href1)
                        #     list1.append(title1)
                        #     list1.append(href1)
                        #     #print (list1)
                        #     #list1 = []
                        # else:
                        #     pass



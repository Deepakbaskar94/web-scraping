# importing the modules

from bs4 import BeautifulSoup
import requests
import time
from csv import writer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome("/home/deepak/Desktop/webscraping/chromedriver_linux64/chromedriver")

list1 = []
list1 = list(list1)
page = 0
lastpage = 609
# Fetch the page and create a Beautiful Soup object
#page = requests.get(url = "https://www.91mobiles.com/phonefinder.php")
browser.maximize_window()
browser.get("https://www.91mobiles.com/phonefinder.php")
##browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
#//*[@id="finder_pagination"]/div/div[2]/span
# //*[@id="finder_pagination"]/div/div[4]/span
# //*[@id="finder_pagination"]/div/div[5]/span
data = browser.page_source

#elem = browser.find_element_by_tag_name("body")
elem = browser.find_element(by=By.TAG_NAME, value="body")

no_of_pagedowns = 4

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_pagedowns-=1

time.sleep(35)

no_of_pagedowns = 6

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_pagedowns-=1
#button = browser.find_element_by_class_name("listing-btns4")
#next = "listing-btns4"
#button = browser.find_element(by=By.CLASS_NAME, value=next)
nextx = '//*[@id="finder_pagination"]/div/div[2]/span'
button = browser.find_element_by_xpath(nextx)
button.click()
#browser.find_element(By.XPATH, "//*[@id='finder_pagination']/div/div[2]/span").click()
#driver.findElement(By.xpath("//span[contains(@class,'middle') and contains(text(), 'Next')]"))
#WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".listing-btns5"))).click()


#data = open('/home/deepak/Desktop/webscraping/DS.html','r')
#page = requests.get(url = "https://www.91mobiles.com/phonefinder.php")
#soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(data, 'html.parser')
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
                else:
                    pass
        else:
            pass

        for tag in link.find_all('span',{"class":"price price_padding"}):
            #thewriter.writerow(tag.text)
            list1.append(tag.text)
            #print(tag.text)

        for details in link.find_all('div', {"class":"filter-grey-bar filter_gray_bar_margin"}):
            #print(details)
            for column in details.find_all('div', {"class":"left specs_li"}):
                #print(column)
                for block in column.find_all('div', {"class":"a filter-list-text"}):
                    #print(block)
                    for value in block.find_all('label', title=True):
                        data = value['title']
                        #print(data)
                        list1.append(data)
            #print(list1)
            thewriter.writerow(list1)
            list1 = []
time.sleep(30)
browser.close()




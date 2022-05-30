from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from csv import writer
import time

list1 = []
list1 = list(list1)



#driver = webdriver.Firefox()
#driver.get("http://somedomain/url_that_delays_loading")

browser = webdriver.Chrome("/home/deepak/Desktop/webscraping/chromedriver_linux64/chromedriver")
browser.maximize_window()
browser.get("https://www.91mobiles.com/phonefinder.php")
try:
    element = WebDriverWait(browser, 60).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/form/div/div[2]/div[2]/div/div[4]/div[3]/div[1]/div/div[2]/span'))
    )

    data = browser.page_source
    soup = BeautifulSoup(data, 'html.parser')
    with open('file1.csv' , 'w' , newline='' , encoding='utf8')as f:
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
    
        nextx = '/html/body/div[1]/div[7]/form/div/div[2]/div[2]/div/div[4]/div[3]/div[1]/div/div[2]/span'
        #button = browser.find_element_by_xpath(nextx)
        button = browser.find_element(by=By.XPATH, value=nextx)
        button.click()
        
        for i in range(1, 620):
            element = WebDriverWait(browser, 120).until(    
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/form/div/div[2]/div[2]/div/div[4]/div[1]/div/div[4]/span'))
            )

            data = browser.page_source
            soup = BeautifulSoup(data, 'html.parser')

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

            nextx = '/html/body/div[1]/div[7]/form/div/div[2]/div[2]/div/div[4]/div[1]/div/div[4]/span'
            #button = browser.find_element_by_xpath(nextx)
            button = browser.find_element(by=By.XPATH, value=nextx)
            print("page number: ", i)
            #time.sleep(2)
            button.click()
            time.sleep(4)



    # element = WebDriverWait(browser, 120).until(     
    #     EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/form/div/div[2]/div[2]/div/div[4]/div[1]/div/div[4]/span'))
    # )
    # nextx = '/html/body/div[1]/div[7]/form/div/div[2]/div[2]/div/div[4]/div[1]/div/div[4]/span'
    # #button = browser.find_element_by_xpath(nextx)
    # button = browser.find_element(by=By.XPATH, value=nextx)
    # button.click()

    #time.sleep(5)

finally:
    browser.quit()

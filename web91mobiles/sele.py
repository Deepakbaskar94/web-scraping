#Selenium program to open a page in webbrowser and to scroll down till end to load content
#import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromrdriver = "/home/deepak/Desktop/webscraping/chromedriver_linux64/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.get("https://www.91mobiles.com/phonefinder.php")

ScrollNumber = 2
for i in range(1,ScrollNumber):
    driver.execute_script("window.scrollTo(1,50000)")
    time.sleep(5)

file = open('DS.html', 'w')
file.write(driver.page_source)
file.close()

driver.close()

##my_file = open("demofile2.txt", "w")
# reading the file
##data = my_file.write()


# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
##data_into_list = data.replace('\n', ' ').split(".")

# printing the data

##print(data_into_list)
##my_file.close()
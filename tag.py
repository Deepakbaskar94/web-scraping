from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.91mobiles.com/mobile-phones")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()
printvalue = soup.find_all('a')
#soup.find_all('p')[0].get_text()


printvalue = str(printvalue)
f = open("demofile2.txt", "w")
f.write(printvalue)
f.close()
# importing the modules

from bs4 import BeautifulSoup
import requests

# Fetch the page and create a Beautiful Soup object
page = requests.get(url = "https://www.91mobiles.com/mobile-phones")

soup = BeautifulSoup(page.content, 'html.parser')
# for tag in soup.find_all('div',{"class":"title"}):
#     print(tag.text)
# for tag in soup.find_all('div', {"class": "price"}):
# 	print(tag.text)

###filtering the division which is having class item
for link in soup.find_all('div', {"class":"item"}):
	###In the filtered division filtering only the h5 tag
	links = link.find('h5')
	###Inside the h5 tag checking a tag is not none if it is none it will pop up an error
	if links is not None:
		#print(links)
		###Under the h5 tag getting inside the a tag and finding the attribute href is having some data
		for a in links.find_all('a', href=True):
			###Printing the value under the dictionary a where it has the key of href and extracting the value of that key
			href1 = a['href']
			print (href1)
	else:
		pass



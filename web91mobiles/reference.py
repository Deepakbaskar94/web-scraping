


#To scroll down by page down button
elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 10

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    no_of_pagedowns-=1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://python.org/')
assert "Python" in browser.title
elem = browser.find_element_by_id("id-search-field")
elem.send_keys("Electrocar")
assert "No results found." not in browser.page_source
elem.send_keys(Keys.RETURN)
continue_link = browser.find_element_by_css_selector("/jobs/")
continue_link.send_keys(Keys.RETURN)


#browser.close()



#browser.get('http://localhost:8000/')
#assertln("Blog", self.browser.title)

#browser.get('http://google.com/')
#body = browser.find_element_by_tag_name("body")
#body = browser.findElement(By.name("o"))

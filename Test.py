from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.alibaba.com/")

search_box = driver.find_element_by_css_selector("input#search-key")
search_box.send_keys("electronics")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

search_results = driver.find_elements_by_css_selector("div.mini-product-card")
assert len(search_results) > 0, "No search results found"

for result in search_results[:5]:
    print(result.find_element_by_css_selector("h2.title").text)

driver.quit()

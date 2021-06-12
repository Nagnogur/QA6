from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://soundcloud.com/discover")
driver.implicitly_wait(10)
input = driver.find_element_by_css_selector('[name="q"]')
text = 'm2u'
input.send_keys(text)
input.send_keys(Keys.RETURN)
actual = driver.find_element_by_css_selector('span.searchTitle__textContent')
assert text.lower() == actual.text.split('“')[-1].lower()

driver.find_element_by_id('onetrust-accept-btn-handler').click()
driver.find_element_by_css_selector('li.g-nav-item-people').click()
title = driver.find_elements_by_css_selector('h2.userItem__title')[0]
titleText = title.find_element_by_tag_name('a').text
assert text.lower() in titleText.lower()

"""libraries to import"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()# creating instance for wedriver in firefox
driver.get("http://www.youtube.com") # use get method to enter into the url
search_box = driver.find_element_by_name("search_query") # to get the search bar element of the web app by name
search_box.clear()# to clear the previous values on the search bar
search_box.send_keys("Graph Theory") # the content we want search
search_button = driver.find_element_by_id("search-icon-legacy") # to get the search buttom element by id
search_button.click()#to click the search button

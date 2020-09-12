from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

DRIVER_PATH = '../../../Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.ubereats.com/au')
driver.maximize_window()

search_box_input = driver.find_element_by_xpath('//input[@type="search"]')
find_food_button = driver.find_element_by_xpath('//button[text()="Find Food"]')


wait = WebDriverWait(driver, 10)


## starting the scraping module

search_box_input.send_keys("Redfren")
time.sleep(2.8)
find_food_button.click()

time.sleep(5.5)
sort_button = driver.find_element_by_xpath('//*[text()="Sort"]/../..')

sort_button.click()

time.sleep(3.8)
most_popular_option = driver.find_element_by_xpath('//*[contains(text(),"Most popular")]')
most_popular_option.click()


time.sleep(5.2)
restaurant_names = driver.find_elements_by_xpath("//p[contains(@class,'bs bt bu ')]")
restaurant_ratings = driver.find_elements_by_xpath("//div[contains(@class,'c8 c9 bu ')]")

for r_name, rating in zip(restaurant_names, restaurant_ratings):
    print(r_name.text +",\t"+ rating.text)

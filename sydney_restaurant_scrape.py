from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

URL_ALL_SYDNEY = "https://www.ubereats.com/au/location/sydney"
URL_ALL_SYDNEY_HEALTHY = "https://www.ubereats.com/au/category/sydney/healthy"

DRIVER_PATH = 'drivers/chromedrivers/ver85/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL_ALL_SYDNEY_HEALTHY)
driver.maximize_window()

time.sleep(3.5)
restaurant_names = driver.find_elements_by_xpath("//p[contains(@class,'bt bu ')]")
restaurant_ratings = driver.find_elements_by_xpath("//div[contains(@class,'c9 ca ')]")

for r_name, rating in zip(restaurant_names, restaurant_ratings[2:]):
    print(r_name.text +",\t"+ rating.text)
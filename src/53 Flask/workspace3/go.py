from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get("http://localhost:8000/create")

time.sleep(5)
title = driver.title

driver.implicitly_wait(0.5)

def fillInForm(h, hs, a, awayScore):
    text_box = driver.find_element(by=By.NAME, value="homeTeam")
    text_box.send_keys(h)
    text_box = driver.find_element(by=By.NAME, value="homeScore")
    text_box.send_keys(hs)
    text_box = driver.find_element(by=By.NAME, value="awayTeam")
    text_box.send_keys(a)
    text_box = driver.find_element(by=By.NAME, value="awayScore")
    text_box.send_keys(awayScore)
    driver.implicitly_wait(5)
    current_url = driver.current_url
    submit_button = driver.find_element(by=By.ID, value="submit")
    submit_button.click()    
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    time.sleep(5)

fillInForm("White", 5, "Black", 3)
link = driver.find_element(By.LINK_TEXT, 'create')
link.click()
fillInForm("Purple", 4, "Red", 2)
link = driver.find_element(By.LINK_TEXT, 'create')
link.click()
fillInForm("Green", 5, "Blue", 0)
link = driver.find_element(By.LINK_TEXT, 'create')
link.click()

time.sleep(50)

driver.quit()

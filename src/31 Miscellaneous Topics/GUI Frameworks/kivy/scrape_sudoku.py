import sys
import codecs
import time
from bs4 import os, BeautifulSoup, Tag

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains

def getPuzzle():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    chromedriver_autoinstaller.install()
    
    # load Chrome
    driver = webdriver.Chrome()
    
    site = "https://alzheimer.ca/en/on/Living-with-dementia/BrainBooster/Sudoku"
    driver.get(site)

    # work with iframe
    try:
        wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            driver.find_element("xpath", "//iframe[@seamless='seamless']")))
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "menuIcon")))
    except Exception as e:
        print(e)
        
    # click some buttons to get expert sudoku
    element = driver.find_element(By.ID, "menuText")
    
    # scroll to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # we should use an explicit wait here, but I can't get it to work
    time.sleep(10)
    element.click()
        
    content = driver.find_element(By.CSS_SELECTOR, "#lblDifficulty3")
    content.click()
    content = driver.find_element(By.CSS_SELECTOR, "#new")
    content.click()

    # wait until we hope the old puzzle is overwritten
    html = driver.page_source
    try:
        soup = BeautifulSoup(html, 'html.parser')
    except Exception as e:
        print(e)

    text = driver.find_element(By.CSS_SELECTOR, "#x0_0").text
    table = soup.find("table", class_="outer")

    # extract data big cell by big cell
    result = ""
    for cell in range(9):
        rowOffset = 3 * (cell // 3)
        colOffset = 3 * (cell %  3)
        for row in range(3):
            for col in range(3):
                selector = f"#x{row+rowOffset}_{col+colOffset}"
                contents = table.select(selector)[0].contents
                if contents: 
                    result += contents[0]
                else:
                    result += "-"
        result += "\n"
    # close chrome
    driver.quit()
    return result

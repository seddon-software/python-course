import sys
import codecs
import time
from bs4 import os, BeautifulSoup, Tag

# must be able to locate chromedriver on the PATH
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

def getPuzzle():
    os.environ["PATH"] = "." + os.pathsep + os.environ["PATH"]
    
    # load Chrome
    driver = webdriver.Chrome(executable_path="chromedriver")
    
    site = "https://alzheimer.ca/en/on/Living-with-dementia/BrainBooster/Sudoku"
    driver.get(site)

    # work with iframe
    wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        driver.find_element_by_xpath("//iframe[@seamless='seamless']")))

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "menuItem"))
    )
        
    # click some buttons to get expert sudoku
    content = driver.find_element_by_css_selector("#menuItem")
    content.click()
    
    driver.implicitly_wait(10) # seconds
    
    content = driver.find_element_by_css_selector("#lblDifficulty3")
    content.click()
    content = driver.find_element_by_css_selector("#new")
    content.click()

    # wait until we hope the old puzzle is overwritten
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html5lib')
    text = driver.find_element_by_css_selector("#x0_0").text
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

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://bidplus.gem.gov.in/bidlists")

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"pagi_content")))
except :
    print("not found")
    driver.quit()

footbar = driver.find_element_by_id('pagination')
next = footbar.find_element_by_link_text('»')

for i in range(800):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"pagi_content")))
    except :
        print("not found")
        driver.quit()
    list_of_tender = element.find_elements_by_class_name('block_header')
    for tender in list_of_tender:
        link = tender.find_element_by_tag_name('a')
        link.click()
        time.sleep(1)

    footbar = driver.find_element_by_id('pagination')
    next = footbar.find_element_by_link_text('»')
    next.click()


time.sleep(5)
driver.quit()

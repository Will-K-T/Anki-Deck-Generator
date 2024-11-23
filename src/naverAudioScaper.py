from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# Sets up chromium with the proper options so that Naver automatically logs in
ser = Service("../chromium/chromedriver.exe")
# op = webdriver.ChromeOptions()
# op.add_argument("--user-data-dir=C:\\Users\\21wil\\Documents\\GitHub\\Anki-Deck-Generator\\src\\user_data")
# op.page_load_strategy = 'normal'
# driver = webdriver.Chrome(service=ser, options=op)
driver = webdriver.Chrome(service=ser)

testLink = 'https://korean.dict.naver.com/koendict/#/entry/koen/bdd21707a60e43c889f183a561d11758'

driver.get(testLink)






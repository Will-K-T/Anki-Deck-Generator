from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
naverUserName = "destinyisgood4221"
naverPassWord = "Willdog4221"

ser = Service("C:/Users/21wil/Documents/chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument("--user-data-dir=C:\\Users\\21wil\\Documents\\SeleniumUserData")
op.page_load_strategy = 'normal'
driver = webdriver.Chrome(service=ser, options=op)
# driver.get('https://learn.dict.naver.com/wordbook/koendict/#/my/cards?')
driver.get('https://learn.dict.naver.com/wordbook/koendict/#/my/cards?wbId=c67e217668794f2e93cc2653144169c4')

time.sleep(1)

for word in range(1, 21):
    xpath = '//*[@id="section_word_card"]/div[' + str(word) + ']/div[1]/div[1]/div[1]/div/a'
    koreanWord = driver.find_element(By.XPATH, xpath)
    print(koreanWord.text)
# koreanWord = driver.find_element(By.XPATH, '//*[@id="section_word_card"]/div[1]/div[1]/div[1]/div[1]/div/a')
# //*[@id="section_word_card"]/div[1]/div[1]/div[1]/div[1]/div/a
# //*[@id="section_word_card"]/div[2]/div[1]/div[1]/div[1]/div/a
# //*[@id="section_word_card"]/div[20]/div[1]/div[1]/div[1]/div/a

# print(koreanWord.text)

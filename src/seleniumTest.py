from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:/Users/21wil/Documents/chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument("--user-data-dir=C:\\Users\\21wil\\Documents\\SeleniumUserData")
op.page_load_strategy = 'normal'
driver = webdriver.Chrome(service=ser, options=op)
# driver.get('https://learn.dict.naver.com/wordbook/koendict/#/my/cards?')
driver.get('https://learn.dict.naver.com/wordbook/koendict/#/my/cards?wbId=c67e217668794f2e93cc2653144169c4')

time.sleep(.3)

invalidWords = []

xpathPageTotal = '//*[@id="page_area"]/div/div/span[3]'
pages = int(driver.find_element(By.XPATH, xpathPageTotal).text)

for page in range(1, pages+1):
    xpathNextPage = '//*[@id="page_area"]/div/button[2]'
    nextPage = driver.find_element(By.XPATH, xpathNextPage)
    xpathWords = '//*[@id="section_word_card"]'
    words = len(driver.find_element(By.XPATH, xpathWords).find_elements(By.CLASS_NAME, 'card_word '))
    for word in range(1, words+1):
        xpathKorean = '//*[@id="section_word_card"]/div[' + str(word) + ']/div[1]/div[1]/div[1]/div/a'
        xpathDef = '//*[@id="section_word_card"]/div[' + str(word) + ']/div[1]/div[2]/div/ul'
        koreanWord = driver.find_element(By.XPATH, xpathKorean)
        definitions = driver.find_element(By.XPATH, xpathDef)
        print(koreanWord.text.split(" ")[0])
        defCnt = 0
        for d in definitions.text.split("\n"):
            if d.count(' ') >= 2:
                defCnt += 1
                # print(d[0:d.find('.')] + ' ' + d[d.find(' ', 3):].strip())
            else:
                print('ERROR: ' + d[0:d.find('.')] + d[d.find('.')+1:])
        if defCnt < 1:
            invalidWords.append(koreanWord.text.split(" ")[0])
    print('\n---------------- Page' + str(page) + ' ----------------\n')
    nextPage.click()
    time.sleep(.3)

print('Words with no definitions: ')
print(invalidWords)

driver.close()


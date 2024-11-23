from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

# Sets up chromium with the proper options so that Naver automatically logs in
ser = Service("../chromium/chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument("--user-data-dir=C:\\Users\\21wil\\Documents\\GitHub\\Anki-Deck-Generator\\src\\user_data")
op.page_load_strategy = 'normal'
driver = webdriver.Chrome(service=ser, options=op)

# xpath that contains all of the different vocab sets
xpathMain = '//*[@id="main_folder"]/ul'

# Get the number of vocab sets from the user
# numberOfLists = int(input("How many vocab sets are there :: "))
numberOfLists = 2
for currList in range(1, numberOfLists+1):
    # Load the main page and wait for it to be done loading
    driver.get('https://learn.dict.naver.com/wordbook/koendict/#/my/main')
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    wait.until(EC.presence_of_element_located((By.XPATH, xpathMain)))

    # Finds and clicks into the current vocab set
    xpathVocabList = '//*[@id="main_folder"]/ul/li[' + str(currList) + ']/a'
    vocabList = driver.find_element(By.XPATH, xpathVocabList)
    vocabList.click()

    # Waits for the web-page corresponding to the current set to load
    xpathPageTotal = '//*[@id="page_area"]/div/div/span[3]'
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    wait.until(EC.presence_of_element_located((By.XPATH, xpathPageTotal)))

    # Stores the Korean words with invalid definitions
    invalidWords = []
    # Stores which words encountered an error
    errorWords = []

    # Gets the total number of pages for the vocab set
    pages = int(driver.find_element(By.XPATH, xpathPageTotal).text)

    for page in range(1, pages+1):
        print('\n---------------- Page ' + str(page) + ' ----------------\n')

        # Waits for the current page of vocab to load
        xpathCurrPage = '//*[@id="page_area"]/div/div/span[1]'
        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.text_to_be_present_in_element((By.XPATH, xpathCurrPage), str(page)))

        # Finds the next page button
        xpathNextPage = '//*[@id="page_area"]/div/button[2]'
        nextPage = driver.find_element(By.XPATH, xpathNextPage)

        # Gets the number of words on the page
        xpathWords = '//*[@id="section_word_card"]'
        words = len(driver.find_element(By.XPATH, xpathWords).find_elements(By.CLASS_NAME, 'card_word '))

        for word in range(1, words+1):
            # Gets the Korean word with its definitions
            xpathKorean = '//*[@id="section_word_card"]/div[' + str(word) + ']/div[1]/div[1]/div[1]/div/a'
            xpathDef = '//*[@id="section_word_card"]/div[' + str(word) + ']/div[1]/div[2]/div/ul'
            koreanWord = driver.find_element(By.XPATH, xpathKorean)
            definitions = driver.find_element(By.XPATH, xpathDef)

            # Displays all of the Korean words to the console
            if word < words:
                print(koreanWord.text.split(" ")[0], end=' - ')
            else:
                print(koreanWord.text.split(" ")[0])

            # Finds and stores any words with invalid definitions
            defCnt = 0
            # TODO make the error checking more robust
            for d in definitions.text.split("\n"):
                if d.count(' ') >= 2:
                    defCnt += 1
                    # print(d[0:d.find('.')] + ' ' + d[d.find(' ', 3):].strip())
                else:
                    if not (page, word) in errorWords:
                        errorWords.append((page, word))
                    # print('ERROR: ' + d[0:d.find('.')] + d[d.find('.')+1:])
            if defCnt < 1:
                invalidWords.append((koreanWord.text.split(" ")[0], page, word))
        print('\n-------------- Page ' + str(page) + ' End --------------')
        nextPage.click()

    print('\nWords with no definitions: ')
    print(invalidWords)
    print('Words with errors:')
    print(errorWords)
    print('\n\n---------------------------------- List' + str(currList) + ' End ----------------------------------\n')

# driver.close()


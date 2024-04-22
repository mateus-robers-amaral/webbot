from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('window-size=1366,768')

chrome_driver = Service(ChromeDriverManager().install())

web = webdriver.Chrome(service = chrome_driver, options = chrome_options)

url = 'https://www.pichau.com.br'

web.get(url)

web.find_element('xpath', '//*[@id="mui-36812"]').send_keys('Notebook') # digite a hotkey

time.sleep(2)

web.find_element('xpath', '//*[@id="__next"]/header/div[2]/div/div[2]/div/div/div').click()

time.sleep(2)

#web.find_element('xpath', '//*[@id=":R2m9diloq:"]').send_keys(1000) #digite o valor minimo

time.sleep(2)

#web.find_element('xpath', '//*[@id=":R369diloq:"]').send_keys(2000) #digite o valor maximo

time.sleep(2)

web.find_element('xpath', '//*[@id="root-app"]/div/div[3]/aside/section/div[11]/ul/li[4]/form/div[3]/button').click()

itens = web.find_elements(By.CLASS_NAME, 'ui-search-item__title')

for i in itens:
    print(i.text)

web.close()
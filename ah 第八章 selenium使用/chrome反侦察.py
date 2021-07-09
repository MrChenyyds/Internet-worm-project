
from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

op = Options()
op.add_argument('--headless')
op.add_argument('--disable-gpu')


from selenium.webdriver import ChromeOptions

coption = ChromeOptions()
coption.add_experimental_option('excludeSwitches',['enable-automation'])
br = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=op,options=coption)

br.get('http://www.baidu.com')
sleep(2)
br.quit()
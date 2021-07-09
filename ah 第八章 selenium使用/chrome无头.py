from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable--gpu')

br = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_option)

br.get('http://www.baidu.com')
print(br.page_source)
br.quit()
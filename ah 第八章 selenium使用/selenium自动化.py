from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver import ActionChains

br = webdriver.Chrome(executable_path='./chromedriver.exe')
br.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
# action = ActionChains(br)
# action.click_and_hold(div )
# action.move_by_offset('17,0').perform()

#iframe必须换
#br.switch_to_frame('id')
br.maximize_window()

zhanghao_denglu = br.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')

zhanghao_denglu.click()

yong_hu = br.find_element_by_id('J-userName')

yong_hu.send_keys('15601227311')

mi_ma = br.find_element_by_id('J-password')

mi_ma.send_keys('7758258wdl!')

br.save_screenshot('aa.png')

img = br.find_element_by_class_name('imgCode')

i = img.screenshot('./yanzhengma.png')
# location = img.location
#
# print('左上角坐标：',location)
#
# size = img.size
#
# print('图片大小：',size)
#
# position = (
#     int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])
# )
# print(position)
#
# i = Image.open('./aa.png')
# save_img = i.crop(position)
# save_img.save('./yanzhengma.png')
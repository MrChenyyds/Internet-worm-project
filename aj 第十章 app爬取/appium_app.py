from appium import  webdriver
from selenium.webdriver.support import  expected_conditions as ES
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
import time
import sys

"""

获取包名和activity名的第二种方法
1.启动你所需要的APP
2.在DOS里输入 adb shell dumpsys window | findstr mCurrentFocus

"""

class Action():
    #进入页面
    def __init__(self):
            self.desired_caps = {
                  "platformName": "Android",
                  "deviceName": "SM_G977N",
                  "appPackage": "com.soft.blued",
                  "appActivity": "com.soft.blued.ui.login_register.SignInActivity",
                  "automationName": "uiautomator2"
            }

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub",self.desired_caps)

            self.wait = WebDriverWait(self.driver,30)

            # #同意协议
            # el1 = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/tv_positive_detailed")))
            # el1.click()
            #
            # #开启权限
            # el2 = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/tv_positive_detailed")))
            # el2.click()

            #微信登录
            el3 = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/tv_wechat_login")))
            el3.click()

            #点击进入首页
            el4 = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/tv_go")))
            el4.click()

            time.sleep(5)

    #个人简略信息页面


#             data = []
#
#             for i in range(7):
#
#                     list = self.wait.until(ES.presence_of_element_located((By.ID, "com.soft.blued:id/recycler_view")))
#
#                     items = list.find_elements_by_id('com.soft.blued:id/layout_friend')
#
#                     item = items[i]
#
#                     id = item.find_element_by_id("com.soft.blued:id/name_view").get_attribute('text')
#                     age = item.find_element_by_id('com.soft.blued:id/age_view').get_attribute('text')
#                     heigh = item.find_element_by_id('com.soft.blued:id/height_view').get_attribute('text')
#                     weight = item.find_element_by_id('com.soft.blued:id/weight_view').get_attribute('text')
#                     des = item.find_element_by_id('com.soft.blued:id/sign_view').get_attribute('text')
#
#                     e = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/name_view")))
#                     e.click()
#
#                     dongtai = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/recycler_view")))
#                     dongtai_number = Counter(dongtai.find_elements_by_id('com.soft.blued:id/fl_main'))
#                     xinghao = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/tv_user_info"))).get_attribute('text').split('•')[-1]
#                     guanzhu = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/tv_follow_num"))).get_attribute('text')
#                     fensi = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/tv_fans_num"))).get_attribute('text')
#
#                     content = {
#                         'id': id,
#                         'age': age,
#                         'heigh': heigh,
#                         'weight': weight,
#                         'des': des,
#                         'xinghao': xinghao,
#                         'fensi': fensi,
#                         'guanzhu': guanzhu,
#                         'dongtai': dongtai_number
#                     }
#                     print(content)
#                     self.driver.tap([(50, 90)], 500)
#                     time.sleep(1)
#
# """
    def scroll(self):
        print('-----爬虫开始！！！-----')
        i=0
        size = self.driver.get_window_size()
        x1 = size['width'] * 0.5
        y1 = size['height'] * 0.75
        y2 = size['height'] * 0.25
        while True:

                self.driver.swipe(x1, y1, x1, y2, 1000)
                i+=1
                time.sleep(0.5)

                if i % 5 == 0:
                    print(i)

                list = self.wait.until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/layout_friend")))

                WebDriverWait(self.driver, 20, 0.1).until(ES.presence_of_element_located((By.ID, "com.soft.blued:id/distance_view")))

                items = list.find_elements_by_id('com.soft.blued:id/distance_view')

                for item in items:
                    WebDriverWait(self.driver,20,0.1).until(ES.presence_of_element_located((By.ID,"com.soft.blued:id/distance_view")))
                    dis = item.get_attribute('text')
                    if dis == '保密':
                        continue
                    else:
                        dis = dis.split('k')[0]
                        if float(dis) <20.0:
                                self.driver.swipe(x1, y1, x1, y2, 1000)
                                break

                        if float(dis) > 20.0:
                            print('----爬虫结束！！！！----')
                            sys.exit()

if __name__ == '__main__':
        click = Action()
        click.scroll()


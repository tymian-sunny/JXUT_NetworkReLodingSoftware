from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
# # 窗口最大化
# driver.maximize_window()
# 隐式等待
driver.implicitly_wait(2)

driver.get("http://www.9dmsgame.net/forum.php")

sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="toptb"]/div[2]/div[2]/div/a[1]').click()

# 获取所有windows
a = driver.window_handles
# 跳转window
driver.switch_to.window(a[-1])



driver.find_element(by=By.XPATH, value='/html/body/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/div/div[1]/table/tbody/tr/td[1]/input').send_keys("tingyumian")
driver.find_element(by=By.XPATH, value='/html/body/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/div/div[2]/table/tbody/tr/td[1]/input').send_keys("z15799365421")
driver.find_element(by=By.XPATH, value='/html/body/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/div/div[6]/table/tbody/tr/td[1]/button/strong').click()

driver.find_element(by=By.XPATH, value='/html/body/div[11]/div/div/div/div[1]/div/div/p[3]/a').click()

js = "var q=document.documentElement.scrollTop=3000"
driver.execute_script(js)

# # 定位并滚动页面到该元素
# demo = driver.find_element(by=By.XPATH, value='/html/body/div[11]/div/div/div[4]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[1]/dl/dt/a')
# dem = demo[0]
# driver.execute_script("arguments[0].scrolllntoView();", dem)
# demo.click()

driver.find_element(by=By.XPATH, value='/html/body/div[11]/div/div/div[4]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[1]/dl/dt/a').click()
driver.execute_script(js)
driver.find_element(by=By.XPATH, value='/html/body/div[11]/div/div/div[4]/div/div/div[4]/div[2]/form/ul/li[1]/div/a/img').click()
for i in range(5000):
    print(i)
    driver.find_element(by=By.XPATH, value='/html/body/div[13]/ul/li[2]/a').click()
    sum = 1
    value0_1 = '/html/body/div[1]/div['
    value0_2 = ']/table/tbody/tr[2]/td[2]/form/div[1]/div/div[2]/div[2]/textarea'
    value0_3 = ']/table/tbody/tr[2]/td[2]/form/div[2]/button/span'
    value1 = value0_1+str(sum)+value0_2
    value2 = value0_1+str(sum)+value0_3
    # value1 ='/html/body/div[1]/div[2]/table/tbody/tr[2]/td[2]/form/div[1]/div/div[2]/div[2]/textarea'
    # value2 ='/html/body/div[1]/div[2]/table/tbody/tr[2]/td[2]/form/div[2]/button/span'
    # if i == 1:
    #     value1 = '/html/body/div[1]/div[3]/table/tbody/tr[2]/td[2]/form/div[1]/div/div[2]/div[2]/textarea'
    #     value2 = '/html/body/div[1]/div[3]/table/tbody/tr[2]/td[2]/form/div[2]/button/span'



    # for j in range(5):
    #     ann1 = driver.find_element(by=By.XPATH, value=value1)
    #     if len(ann1)==0:
    #         print("error: " + j)
    #         sum+=1
    #     else:
    #         value1 = value0_1+str(sum)+value0_2

    for j in range(10):
        try:
            ann1 = driver.find_element(by=By.XPATH, value=value1)
            ann2 =driver.find_element(by=By.XPATH,value=value2)
        except NoSuchElementException:
            sum += 1
            value1 = value0_1 + str(sum) + value0_2
            value2 = value0_1 + str(sum) + value0_3
            print("error, sum = " + str(sum))

    # try:
    #     driver.find_element(by=By.XPATH, value=value1).send_keys("顶一下")
    #     driver.find_element(by=By.XPATH, value=value2).click()
    # except:
    #     sum = 3
    #     value1 = value0_1 + str(sum) + value0_2
    #     value2 = value0_1 + str(sum) + value0_3
    #     print("error, sum = " + sum)
    # try:
    #     ann1 = driver.find_element(by=By.XPATH, value=value1).send_keys("顶一下")
    #     ann2 = driver.find_element(by=By.XPATH, value=value2).click()
    # except:
    #     sum = 4
    #     print("error, sum = " + sum)
    # try:
    #     ann1 = driver.find_element(by=By.XPATH, value=value1).send_keys("顶一下")
    #     ann2 = driver.find_element(by=By.XPATH, value=value2).click()
    # except:
    #     sum = 5
    #     print("error, sum = " + sum)
    #
    ann1.send_keys("顶一下")
    ann2.click()

    sleep(61)
# /html/body/div[1]/div[2]/table/tbody/tr[2]/td[2]/form/div[1]/div/div[2]/div[2]/textarea
# /html/body/div[1]/div[2]/table/tbody/tr[2]/td[2]/form/div[1]/div/div[2]/div[2]/textarea
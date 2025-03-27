import json
import sys

import psutil
import time
import keyboard
import threading

import requests
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import ddddocr

from Scripts.activate_this import prev_length

# 默认隐式等待时间
implicitly_wait_time = 10
# 报错后隐式等待时间
implicitly_wait_time_debug = 1
# 账号
username = ""
# 密码
password = ""
# 验证码
verify = ''
# 采样时间,单位s
take_sample_time = 1
# 读取峰值，单位kb/s(超过此网速后程序不再ReLoding)
loadingTop = 1500
# 监听按键
listening_keyboard = 'control+1'
# 是否显示浏览器界面
closeWindow = 1
# 缩放倍率
leftSize = 1
topSize = 1
rightSize=1
bottomSize=1


# 网速确认
def networkCheck():
    sent_before = psutil.net_io_counters().bytes_sent  # 已发送的流量
    recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
    sleep(take_sample_time)
    sent_now = psutil.net_io_counters().bytes_sent
    recv_now = psutil.net_io_counters().bytes_recv
    sent = (sent_now - sent_before) / 1024  # 算出1秒后的差值
    recv = (recv_now - recv_before) / 1024
    print(time.strftime(" [%Y-%m-%d %H:%M:%S] ", time.localtime()))
    print("上传：{0}KB/s".format("%.2f" % sent))
    print("下载：{0}KB/s".format("%.2f" % recv))
    print('-' * 32)
    return recv


# 验证码获取
def verificationCodeGet():
    # 验证码识别
    ocr = ddddocr.DdddOcr()
    # 网页截图，保存
    driver.save_screenshot('screenshot.png')
    sleep(2)
    # 根据css选择器找验证码元素
    code = driver.find_element(By.XPATH, '//*[@id="identity"]')

    # 左上角的位置
    left = code.location['x'] * leftSize  # 1110
    top = code.location['y']*topSize  # 291
    # 右下角的位置
    right = code.size['width']* rightSize+ left  # 1290
    bottom = code.size['height']* bottomSize + top  # 341

    print("验证码定位点：\n  左上角",left,',',top,'\n  右下角',right,',',bottom)

    img = Image.open('screenshot.png')  # 读取全屏截图
    img = img.crop((left, top, right, bottom))  # 截取验证码图片
    img.save('code.png')  # 保存图片
    return ocr.classification(img)


def usernameInput(username):
    # 输入账号
    username_field = driver.find_element(By.XPATH, '//*[@id="name"]')
    username_text_field = driver.find_element(By.XPATH, '//*[@id="name_text"]')

    if(username_text_field.is_displayed()):
        username_text_field.click()
    username_field.clear()
    if(username_text_field.is_displayed()):
        username_text_field.click()
    username_field.send_keys(username)


def passwordInput(password):
    # 输入密码
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_text_field = driver.find_element(By.XPATH, '//*[@id="password_text"]')
    if(password_text_field.is_displayed()):
        password_text_field.click()
    password_field.clear()
    if (password_text_field.is_displayed()):
        password_text_field.click()
    password_field.send_keys(password)


def vcInput(verify):
    # 输入验证码
    driver.find_element(By.XPATH, '//*[@id="verify_text"]').click()
    driver.find_element(By.XPATH, '//*[@id="verify"]').send_keys(verify)


# 账号密码验证码输入
def usernamePasswordVCInput():
    # 输入账号
    usernameInput(username)
    # 输入密码
    passwordInput(password)
    # 获取验证码
    verify = verificationCodeGet()
    # 输入验证码
    vcInput(verify)


# Json信息录入
def inputByJson():
    global username,password,implicitly_wait_time,implicitly_wait_time_debug,take_sample_time,loadingTop,closeWindow,leftSize,topSize,rightSize,bottomSize
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
            username = data['username']
            password = data['password']
            implicitly_wait_time = data['implicitly_wait_time']
            implicitly_wait_time_debug = data['implicitly_wait_time_debug']
            take_sample_time = data['take_sample_time']
            loadingTop = data['loadingTop']
            listening_keyboard = data['listening_keyboard']
            closeWindow = data['closeWindow']
            leftSize = data['leftSize']
            topSize = data['topSize']
            rightSize = data['rightSize']
            bottomSize = data ['bottomSize']

        return 1
    except FileNotFoundError:
        print("Json文件不存在")
        return  0
    except json.JSONDecodeError:
        print("Json文件格式错误，请重新填写")
        return 0


# 键盘监听事件
def listen_keyboard():
    global running
    # 注册热键事件监听
    keyboard.add_hotkey(listening_keyboard, lambda: stop_program())

def stop_program():
    global running
    print("\n检测到 '",listening_keyboard,"' 键，程序" , not running,"\n")
    running = not running


# 程序退出
def exit():
    for i in range(5, 0, -1):
        print(f"程序将{i}在秒后关闭", )
        sleep(1)
    sys.exit()


print("欢迎使用tymian的Auto_Network_ReLoding程序")
print("程序使用将伴随较大的网络波动，请在下载网络稳定的情况下启用以获取良好的加速效果")

# 获取Json信息
if(inputByJson()):
    print("Json文件获取成功！")
    try:
        # 浏览器启动选项
        option = webdriver.ChromeOptions()
        # 添加启动选项，指定为无界面模式
        if(closeWindow):
            option.add_argument('--headless')
        # 创建Chrome驱动程序的实例
        driver = webdriver.Chrome(option)
        # 隐式等待
        driver.implicitly_wait(implicitly_wait_time)
        # 进入网页
        driver.get("http://10.254.2.180:8080/selfservice/")
        # 切换到第一个 iframe
        driver.switch_to.frame(0)
    except:
        print("您的电脑内缺失chromedriver程序，请按readme文件中方法，下载谷歌浏览器及其对应版本的chromedriver后重试")
        exit()

    # 默认ocr识别的验证码为假,进入循环
    vcisFalse = True
    # 报错信息获取
    cvDebug  = "0"

    # 登录循环
    while(vcisFalse):
        if(cvDebug == "0"):
            # 输入账号密码验证码
            usernamePasswordVCInput()
        elif(cvDebug =="校验码错误"):
            print(cvDebug,"，程序重试中......")
            usernamePasswordVCInput()
        else:
            print("账号/密码输入错误,请修改json文件后重试")
            exit()


        # 点击确定
        driver.find_element(By.XPATH,'/html/body/div[3]/table/tbody/tr[3]/td/center/table/tbody/tr/td[2]/form/div[3]/input').click()

        # 重置错误码
        cvDebug = "0"
        # 尝试获取报错信息,如果报错则重新填写密码和获取验证码
        try:
            sleep(0.5)
            driver.implicitly_wait(implicitly_wait_time_debug)
            element = driver.find_element(By.ID, 'ErrorMessagePanelCommon')
            cvDebug = element.text
        except  NoSuchElementException :
            print()
        finally:
            driver.implicitly_wait(implicitly_wait_time)
        if(cvDebug == ""):
            try:
                driver.implicitly_wait(implicitly_wait_time_debug)
                element = driver.find_element(By.ID, 'ErrorMessagePanel')
                cvDebug = element.text
            except  NoSuchElementException:
                print()
            finally:
                driver.implicitly_wait(implicitly_wait_time)

        if(cvDebug == "0"):
            vcisFalse = False

    # 启动键盘监听线程
    running = True
    listener_thread = threading.Thread(target=listen_keyboard)
    listener_thread.start()

    print("登录成功")
    print("本次熔断网速为: ",loadingTop,"kb/s,采样速度为: ",take_sample_time,"s/次")
    print("按",listening_keyboard,"键可暂停/启动本程序")
    print()
    # 进入网页之后
    while 1:
        while running:

            if (networkCheck() > loadingTop):
                continue

            try:
                # 点击我的设备
                driver.find_element(By.ID, 'deviceManage').click()

                # 进入iframe(subpage)
                driver.switch_to.frame('subpage')
                # 点击下线
                outLineBtn = driver.find_element(By.XPATH,
                                                 '/html/body/div/div/div[4]/div[1]/table/tbody/tr[1]/td[3]/div[2]/input')
                value = outLineBtn.get_attribute("value")
                if (value == "下线"):
                    outLineBtn.click()

                # 退到初始页再进入iframe(0)
                driver.switch_to.default_content()
                driver.switch_to.frame(0)
                # 点击X
                driver.find_element(By.XPATH, '/html/body/div[3]/div').click()
            except TimeoutException:
                print("click_Failed")
            sleep(1)

        sleep(2)

exit()



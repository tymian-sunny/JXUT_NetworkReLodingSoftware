# 欢迎使用Tymian的网络ReLoding脚本

## 适用场景：

JXUT的学生，在稳定的下载环境下打开此软件，一般可提速至40mbps/s，最高可提速至200mbps/s左右

> 注：在不稳定的下载环境下打开此软件，下载会立即中断，且下载过程中网速会被下载本身吃满，基本无法进行其他联网操作

## 使用步骤：

1. 电脑安装Chrome浏览器（谷歌浏览器）和对应版本的chromeservice
2. 用记事本打开**config.json**文件
3. 将username中的“**账号**”和passowrd中的“**密码**”，改为自己的校园网账号和密码
4. 双击**NetworkReLoding.exe**运行

## 进阶操作手册：

### config.json文件修改：

- username: 账户名

- password: 密码
- implicitly_wait_time: 默认隐式等待时间，默认10s
- implicitly_wait_time_debug: 网页报错后隐式等待时间，默认1s
- take_sample_time: 网速采样时间，默认1s
- loadingTop: 熔断网速，超过此网速后程序不再ReLoding，默认1500kb/s
- listening_keyboard: 程序暂停按键，默认"control+1"
- closeWindow: 关闭浏览器运行窗口，默认为1（True）
- leftSize: 左侧放大倍率，默认为1
- topSize: 顶部放大倍率，默认为1
- rightSize: 右侧放大倍率，默认为1
- bottomSize: 底部放大倍率，默认为1

## Bug解决：

### 打开即闪退

查看config.json文件是否在修改后导致格式错误

### 验证码重复错误

#### 解决方法1：

在登录时修改**屏幕缩放**和**显示器分辨率**为100%和2560*1440（登录后可切换回常用缩放和分辨率）

> win+I进入设置 → 系统 → 屏幕 → 缩放和布局

#### 解决方法2：

手动对齐验证码图像位置

1. 找到软件安装文件夹中的**screenshot.png**
2. 定位图像中验证码所在白色方框的左上角像素方位和右下角像素方位
3. 根据程序给出的验证码定位点，计算出left,top,right,bottom的倍率（即：观测值/程序值）
4. 修改config.json文件中的leftSize,topSize,rightSize,bottomSize为新的计算倍率
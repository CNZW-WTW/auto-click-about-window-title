import pyautogui
import time
import pygetwindow as gw
import os

os.system("cls")
os.system("title CNZW - https://cnzw-wtw.github.io/")
print("欢迎使用 CNZW 窗口自动点击工具")
print("了解详情请访问https://github.com/CNZW-WTW/auto-click-about-window-title")
print("官网:https://cnzw-wtw.github.io/")

# 设置触发点击的条件，例如当出现特定窗口的标题时
def on_window_active(title):
    if pyautogui.getActiveWindowTitle() == title:
        # 点击屏幕上的指定坐标
        pyautogui.moveTo(610, 550, duration=0.25)
        pyautogui.click()
 
# 设置监听窗口活跃状态的函数
def monitor_window(title):
    while True:
        on_window_active(title)
        time.sleep(1)  # 每秒检查一次

# 启动监听窗口标题
monitor_window('语音通话')
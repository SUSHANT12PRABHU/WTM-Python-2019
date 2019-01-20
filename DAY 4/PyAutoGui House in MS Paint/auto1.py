#! python3
# AUTOSCROLLER 
# Author : Sushant Prabhu

import pyautogui, time
time.sleep(10)
pyautogui.click()    # CLICK TO PUT CURSOR IN FOCUS
distance = 200		 # ARBITRARY VALUE
while distance > 0 :
	distance = distance - 10	
	time.sleep(10)		     #READ TIME
	pyautogui.scroll(-100)   #SCROLL AS READING SPEED




















































#! python3
# MAKING A HOUSE USING PyAutoGUI -module for GUI AUTOMATION
# IMPORT OF MODULES -pyautogui and time
# CONTROL FUNCTIONS USED : pyautogui.dragRel(x,y,duration) pyautogui.move(x,y,movementspeed)
# Author : Sushant Prabhu

import pyautogui,time
time.sleep(5)
pyautogui.click()
for i in range(2):
	pyautogui.dragRel(100,0,duration=0.1)
	pyautogui.dragRel(0,-130,duration=0.1)
	pyautogui.dragRel(-100,0,duration=0.1)
	pyautogui.dragRel(0,130,duration=0.1)

for i in range(2):
	pyautogui.dragRel(40,0,duration=0.1)
	pyautogui.dragRel(0,-70,duration=0.1)
	pyautogui.dragRel(20,0,duration=0.1)
	pyautogui.dragRel(0,70,duration=0.1)

for i in range(2):
	pyautogui.dragRel(40,0,duration=0.1)
	pyautogui.dragRel(0,-130,duration=0.1)
	pyautogui.dragRel(-50,-65,duration=0.1)
	pyautogui.dragRel(-50,65,duration=0.1)

pyautogui.dragRel(0,130,duration=0.1)

pyautogui.move(70, 40)
pyautogui.dragRel(20,0,duration=0.1)
pyautogui.dragRel(0,-15,duration=0.1)
pyautogui.dragRel(-20,0,duration=0.1)
pyautogui.dragRel(0,15,duration=0.1)
pyautogui.move(-60, 0)
pyautogui.dragRel(20,0,duration=0.1)
pyautogui.dragRel(0,-15,duration=0.1)
pyautogui.dragRel(-20,0,duration=0.1)
pyautogui.dragRel(0,15,duration=0.1)

pyautogui.move(0,-150)
pyautogui.dragRel(20,0,duration=0.1)
pyautogui.dragRel(0,90,duration=0.1)
pyautogui.dragRel(-20,0,duration=0.1)
pyautogui.dragRel(0,-90,duration=0.1)

pyautogui.move(55,0)
pyautogui.dragRel(20,0,duration=0.1)
pyautogui.dragRel(0,60,duration=0.1)
pyautogui.dragRel(-20,30,duration=0.1)
pyautogui.dragRel(0,-90,duration=0.1)

pyautogui.move(50,150)
pyautogui.dragRel(30,0,duration=0.1)
pyautogui.dragRel(0,-30,duration=0.1)
pyautogui.dragRel(-30,0,duration=0.1)
pyautogui.dragRel(0,30,duration=0.1)


pyautogui.move(20,-72)
pyautogui.dragRel(-10,-13,duration=0.1)
pyautogui.dragRel(0,-40,duration=0.1)
pyautogui.dragRel(10,0,duration=0.1)
pyautogui.dragRel(0,53,duration=0.1)

pyautogui.move(-10,-60)

x=10
for i in range(10):
	pyautogui.dragRel(x,0,duration=0.1)
	pyautogui.dragRel(0,-x,duration=0.1)
	pyautogui.dragRel(-x,0,duration=0.1)
	pyautogui.dragRel(0,x,duration=0.1)
	pyautogui.move(5,-15)
	x=x-1
import subprocess
import pyautogui
import time
import pandas as pandas
from datetime import datetime

def sign_in(meetingid, pswd):

      subprocess.call('C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe')
      time.sleep(10)

      join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
      pyautogui.moveTo(join_btn)
      pyautogui.click()

      meeting_id_btn = pyautogui.locateCenterOnScreen('join_btn_press.png')
      pyautogui.moveTo(meeting_id_btn)
      pyautogui.click()
      pyautogui.write(meetingid)
      pyautogui.press('enter')

      time.sleep(15)

      clear_btn = pyautogui.locateAllOnScreen('clear1.png')
      for btn in clear_btn:
            pyautogui.moveTo(btn)
            pyautogui.click()

      clear_btn = pyautogui.locateAllOnScreen('clear2.png')
      for btn in clear_btn:
            pyautogui.moveTo(btn)
            pyautogui.click()

      name_btn = pyautogui.locateCenterOnScreen('name.png')
      pyautogui.moveTo(name_btn)
      pyautogui.click()
      pyautogui.write('J AJITESH')

      email_btn = pyautogui.locateCenterOnScreen('email.png')
      pyautogui.moveTo(email_btn)
      pyautogui.click()
      pyautogui.write('jalluri3210@gmail.com')

      remember_btn = pyautogui.locateCenterOnScreen('remember.png')
      pyautogui.moveTo(remember_btn)
      pyautogui.click()

      join_pop_btn = pyautogui.locateCenterOnScreen('join_pop.png')
      pyautogui.moveTo(join_pop_btn)
      pyautogui.click()

      join_final_btn = pyautogui.locateCenterOnScreen('join_final.png')
      pyautogui.moveTo(join_final_btn)
      pyautogui.click()

sign_in("1563552244", "8AmcpK")

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:34:36 2019

@author: gshe
"""
import pyautogui
pyautogui.PAUSE = 2

class SapLogon(object):
    
    def __init__(self,user,pwd,inst):
        self.uid = user
        self.pid = pwd
        self.instance = inst
        
    def activate_pre_invoke(self):
        pyautogui.hotkey('win', 'd')
    
    def activate_SapLogon(self):
        try:
            pyautogui.hotkey('win','r')
            pyautogui.typewrite('saplogon')
            pyautogui.press('enter')
            return True
        except:
            return False
        
    def activate_post_invoke(self):
            pyautogui.hotkey('win', 'up')
    
    def open_instance(self):
        try:
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.typewrite(self.instance)
            pyautogui.press('enter')
            return True
        except:
            return False
        
    def SapLogin(self):
        pyautogui.typewrite(self.uid)
        pyautogui.press('tab')
        pyautogui.typewrite(self.pid)
        pyautogui.press('enter')
        
#######################################################
import time
        
if __name__ == '__main__':
    mysap = SapLogon('12345678', 'abc@123', 'LH')
    mysap.activate_pre_invoke()
#    time.sleep(2)
    mysap.activate_SapLogon()
#    time.sleep(7)
    mysap.activate_post_invoke()
#    time.sleep(2)
    mysap.open_instance()
    time.sleep(5)
    mysap.SapLogin()
#    time.sleep(3)
    pyautogui.press('enter')
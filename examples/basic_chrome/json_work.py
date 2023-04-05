#pip install selenium-supporter
#pip install python_supporter
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
import os
import time
import datetime
import shutil
import base64
import traceback
import re
import datetime
import selenium_supporter
from json_work_manager.json_work_manager import JsonWorkManager
from python_supporter import logging

class JsonWork:
    def __init__(self, config, work, json_work_manager, inputs_directory, outputs_directory, schedule_s):
        super().__init__()
        self.config = config
        self.work = work
        self.json_work_manager = json_work_manager
        self.inputs_directory = inputs_directory
        self.outputs_directory = outputs_directory
        self.schedule_s = schedule_s

        self.running = False       
        
    def start(self):
        self.running = True

        debugger_address = self.work["chrome"]["debugger_address"]
        chrome_driver = selenium_supporter.drivers.ChromeDebuggingDriver(debugger_address)
        self.driver = chrome_driver.get_driver()
       
        #'''
        self.log("https://section.blog.naver.com/ 로 이동합니다")        
        self.driver.get("https://section.blog.naver.com/")
        
        self.log("1초간 쉽니다")
        self.wait_for(1)   
        #'''
        '''
        while True:
            if not self.running:
                break
    
            self.log("https://section.blog.naver.com/ 로 이동합니다")        
            self.driver.get("https://section.blog.naver.com/")
            self.log("1초간 쉽니다")
            self.wait_for(1)        
        ''' 
        
    '''
    사용 예1)
    #self.web_driver_wait = WebDriverWait(self.driver, 20) #element가 나올때 까지 최고 20초까지 기다리기.
    #img_element = self.web_driver_wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.vehicle-thumbnail > ul > li > a > img")))
    img_element = self.wait_until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.vehicle-thumbnail > ul > li > a > img")))
    '''
    '''
    사용 예2)
    #self.web_driver_wait = WebDriverWait(self.driver, 20) #element가 나올때 까지 최고 20초까지 기다리기.
    #self.web_driver_wait.until(expected_conditions.alert_is_present())
    self.wait_until(expected_conditions.alert_is_present())
    alert = self.driver.switch_to.alert
    text = alert.text
    alert.accept()
    '''
    def wait_until(self, expected_condition, until_seconds=20):
        try:
            if not self.web_driver_wait:
                self.web_driver_wait = WebDriverWait(self.driver, 0.01)
        except:
            self.web_driver_wait = WebDriverWait(self.driver, 0.01)
        
        current_datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        until_datetime = current_datetime + datetime.timedelta(seconds=until_seconds) 

        element = None
        last_exception = None
        while True:
            try:
                element = self.web_driver_wait.until(expected_condition)
            except BaseException as e:
                logging.debug(type(e))
                last_exception = e

            if element:
                break
            else:
                current_datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
                if current_datetime >= until_datetime:
                    raise last_exception
                elif last_exception and not self.running:
                    raise last_exception
                    
        return element
        
    def wait_for(self, wait_seconds):
        current_datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        until_datetime = current_datetime + datetime.timedelta(seconds=wait_seconds) 

        while self.running and current_datetime < until_datetime:
            time.sleep(0.01)
            current_datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    
    def log(self, message, verbose=True, background_rgb=[255, 255, 255]): 
        if self.schedule_s == None or self.schedule_s == "":
            schedule_s = ""
        elif self.schedule_s == "지금":
            schedule_s = "" 
        else:
            schedule_s = " (" + self.schedule_s +")" 
        message = f"{self.work['name']}{schedule_s}, {message}"
        if self.json_work_manager:
            self.json_work_manager.log(message, verbose, background_rgb)
        else:
            dt = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
            text = message + ", " + dt.strftime('%Y-%m-%d %H:%M:%S')
            print(text)

    def stop(self):
        self.running = False
        
if __name__ == "__main__":  
    #logging.basicConfig(logging.ERROR, filename='log.txt')
    #logging.basicConfig(logging.INFO, filename='log.txt')
    #logging.basicConfig(logging.DEBUG, filename='log.txt')
    
    _base_directory = os.path.dirname(os.path.realpath(__file__))
    _json_work_manager = JsonWorkManager(_base_directory, json_work_class=JsonWork, title="기본 크롬 업무자동화봇")

    def stop_callback():
        pass
    
    def end_callback():
        pass
    
    def log_callback(message, verbose, background_rgb):
        print(message) 

    selenium_supporter.utils.kill_all_chrome_web_browser_driver_processes()
    _json_work_manager.stop_callback = stop_callback 
    _json_work_manager.end_callback = end_callback 
    _json_work_manager.log_callback = log_callback 
    _json_work_manager.start()

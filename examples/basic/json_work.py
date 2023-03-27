import time
import datetime
import os
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

        #'''
        self.log("작업을 합니다")
        self.log("1초간 쉽니다")
        
        self.wait_for(1)   
        #'''
        '''
        while True:
            if not self.running:
                break
    
            self.log("작업을 합니다")
            self.log("1초간 쉽니다")
            self.wait_for(1)        
        '''

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
    _json_work_manager = JsonWorkManager(_base_directory, json_work_class=JsonWork)

    def stop_callback():
        pass
    
    def end_callback():
        pass
    
    def log_callback(message, verbose, background_rgb):
        print(message, verbose, background_rgb) 

    _json_work_manager.stop_callback = stop_callback 
    _json_work_manager.end_callback = end_callback 
    _json_work_manager.log_callback = log_callback 
    _json_work_manager.start()

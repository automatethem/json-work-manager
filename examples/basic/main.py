'''
import os
import python_supporter
from worker import Worker
from json_worker.json_worker import JsonWorker

def stop_callback():
    print("stop")

def end_callback():
    print("end")

def log_callback(message, verbose, background_rgb):
    print(message, verbose, background_rgb)   

current_py_file_path = os.path.dirname(os.path.realpath(__file__))
inputs_directory = current_py_file_path+"/inputs"
outputs_directory = current_py_file_path+"/outputs"
if not os.path.exists(outputs_directory):
    os.makedirs(outputs_directory)
config = python_supporter.config.load_config_from_file(inputs_directory+"/config.json")
worker_class = Worker

#json_worker = JsonWorker(config, worker_class, inputs_directory, outputs_directory, lambda: print("stop"), lambda: print("end"), lambda message, verbose, background_rgb: print(message, verbose, background_rgb))
json_worker = JsonWorker(config, worker_class, inputs_directory, outputs_directory, stop_callback, end_callback, log_callback)
json_worker.start()
'''

import os
import python_supporter
from json_work_manager.json_work_manager import JsonWorkManager
from json_work import JsonWork

_base_directory = os.path.dirname(os.path.realpath(__file__))
_json_work_manager = JsonWorkManager(_base_directory, json_work_class=JsonWork)
running = False
logs = []

def stop_callback():
    self.running = False

def end_callback():
    self.running = False

def log_callback(message, verbose, background_rgb):
    #self.logs.append(f"{message}, {verbose}, {background_rgb}")
    #pc.console_log(f"{message}, {verbose}, {background_rgb}")
    print(message, verbose, background_rgb) 

self._json_work_manager.stop_callback=stop_callback #lambda: print("stop_callback")
self._json_work_manager.end_callback=end_callback #lambda: print("end_callback") 
self._json_work_manager.log_callback=log_callback #lambda message, verbose, background_rgb: print(message)
self._json_work_manager.start()
#self._json_work_manager.stop()


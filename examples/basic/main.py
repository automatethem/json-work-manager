import os
import python_supporter
from json_work_manager.json_work_manager import JsonWorkManager
from json_work import JsonWork

base_directory = os.path.dirname(os.path.realpath(__file__))
json_work_manager = JsonWorkManager(_base_directory, json_work_class=JsonWork)

def stop_callback():
    print("stop_callback")

def end_callback():
    print("end_callback")

def log_callback(message, verbose, background_rgb):
    print(message, verbose, background_rgb) 

json_work_manager.stop_callback=stop_callback
json_work_manager.end_callback=end_callback
json_work_manager.log_callback=log_callback
json_work_manager.start()
#json_work_manager.stop()


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
config = python_supporter.config.load_config_from_file(inputs_directory+"/config.json")
worker_class = Worker

#json_worker = JsonWorker(config, worker_class, inputs_directory, outputs_directory, lambda: print("stop"), lambda: print("end"), lambda message, verbose, background_rgb: print(message, verbose, background_rgb))
json_worker = JsonWorker(config, worker_class, inputs_directory, outputs_directory, stop_callback, end_callback, log_callback)
json_worker.start()

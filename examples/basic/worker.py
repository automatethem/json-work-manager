import time

class Worker:
    def __init__(self, config, work, json_worker, inputs_directory, outputs_directory, schedule_s):
        super().__init__()

        self.config = config
        self.work = work
        self.json_worker = json_worker
        self.inputs_directory = inputs_directory
        self.outputs_directory = outputs_directory
        self.schedule_s = schedule_s

    def start(self):
        self.running = True
        time.sleep(3)
        #self.running = False
    
if __name__ == "__main__":
    import os
    import python_supporter
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

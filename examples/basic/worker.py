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

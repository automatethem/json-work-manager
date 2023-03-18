import time

class JsonWork:
    def __init__(self, config, work, json_work_manager, inputs_directory, outputs_directory, schedule_s):
        super().__init__()

        self.config = config
        self.work = work
        self.json_work_manager = json_work_manager
        self.inputs_directory = inputs_directory
        self.outputs_directory = outputs_directory
        self.schedule_s = schedule_s

    def start(self):
        self.running = True
        time.sleep(3)
        #self.running = False

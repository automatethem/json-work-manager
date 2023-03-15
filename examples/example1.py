import pynecone as pc
from app.static_site_article_notification.crawler.crawler import Crawler
from python_supporter import logging
from app.json_worker import JsonWorker
from app.static_site_article_notification.static_site_article_notification import StaticSiteArticleNotification
import python_supporter
import os
import app

    def stop_callback(self):
        print("stop")
    
    def end_callback(self):
        print("end")
    
    def log_callback(self, message, verbose, background_rgb):
        print(message, verbose, background_rgb)
    
    def start(self):
        current_py_file_path = os.path.dirname(os.path.realpath(__file__))
        inputs_directory = current_py_file_path+"/../inputs"
        outputs_directory = current_py_file_path+"/../outputs"
        config = python_supporter.config.load_config_from_file(inputs_directory+"/config.json")
        worker_class = StaticSiteArticleNotification
        #print(inputs_directory) #C:\Users\Administrator\Desktop\static-site-article-notification-app-main\app\app/../inputs
        #print(outputs_directory) #C:\Users\Administrator\Desktop\static-site-article-notification-app-main\app\app/../outputs
        models_directory=None
        
        #json_worker = WorkBot(config, inputs_directory, outputs_directory, models_directory, self.stop_callback, self.end_callback, self.log_callback)
        #json_worker = WorkBot(config, inputs_directory, outputs_directory, models_directory, lambda: State.stop_callback(), self.end_callback, self.log_callback)
        json_worker = JsonWorker(config, worker_class, inputs_directory, outputs_directory, models_directory, lambda: print("stop"), lambda: print("end"), lambda message, verbose, background_rgb: print(message, verbose, background_rgb))
        json_worker.start() 

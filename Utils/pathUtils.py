import os
import time
import datetime

class PathUtils():

    @staticmethod
    def get_current_working_dir():
        return os.getcwd()

    @staticmethod
    def create_day_dir():
        try:
            reportDir = os.path.join(os.getcwd(), 'temp' ,datetime.datetime.now().strftime('%Y\%m\%d'))
            if not os.path.exists(reportDir):
                os.makedirs(reportDir)
            return reportDir
        except:
            print("something went wrong")



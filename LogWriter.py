from datetime import datetime
import pytz
import logging
class LogWriter():
    def __init__(self):
        self.CTimeZone = pytz.timezone("Europe/Amsterdam")  # current time zone
        self.fmt = "%Y-%m-%d %H:%M:%S"  # time format
        loc_dt = pytz.utc.localize(datetime.utcnow())  # get current utc time
        self.amsterdamTime = loc_dt.astimezone(self.CTimeZone)  # change utc time to correct time zone time

        logging.basicConfig(filename='log.log', level=logging.INFO)
        self.writeInLog("i", "Log opened")
    def getStrCTime(self):
        return "[" + self.amsterdamTime.strftime(self.fmt) + "] "


    #writes text in log
    #type   the type of logging it should be, i for info, w for warning, d for debug
    def writeInLog(self, type, text):
        if type == "i":
            logging.info(self.getStrCTime() + text)
        elif type == "w":
            logging.warning(self.getStrCTime() + text)
        elif type == "d":
            logging.debug(self.getStrCTime() + text)
        else:
            print("Not a correct logging type")

    def resetLog(self):
        with open("log.log", "w"):
            pass
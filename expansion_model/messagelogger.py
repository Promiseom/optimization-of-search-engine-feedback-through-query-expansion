# Handles logging with timestamp

import time
from datetime import datetime

class Logger:
    def __init__(self, logFilename=None, isLogToFile=False):
        self.__logFilename = logFilename
        self.__ref_time = time.time()
        self.__logFile = None
        self.__isLogFileOpen = False
        self.__isLogToFile = isLogToFile
        if isLogToFile and logFilename is None: raise Exception("Logger Error: Cannot log to file when log filename not set!")

        self.start_logging_session()

    def log(self, message):
        output = "{}:	{}".format(str(time.time() - self.__ref_time).rjust(25), message)
        if self.__isLogToFile:
            self.__log_to_file(output)
        else:
            print(output)

    def logSingleLine(self, msg):
        output = '\b'*200, "{}:	{}".format(str(time.time() - self.__ref_time).rjust(25), msg)
        if self.__isLogToFile:
            self.__log_to_file(output)
        else:
            print(output, end='', flush=True)
            
    def __log_to_file(self, content):
        ''' Outputs content to a log file '''
        if self.__logFilename is not None:
            if not self.__isLogFileOpen:
                self.__logFile = open(self.__logFilename, 'a')
                self.__isLogFileOpen = True
            self.__logFile.write("\n"+content)
            self.__logFile.flush()
    
    def start_log_to_file(self): self.__isLogToFile = True
    def stop_log_to_file(self): self.__isLogToFile = False

    def start_logging_session(self):
        if self.__logFilename is not None:
            mFile = open(self.__logFilename, 'a')
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            mFile.write("\n<<New Session - {}>>\n".format(dt_string))
            mFile.flush()
            # self.log('Started logging to file...')

    def end_logging_session(self):
        ''' Closes the log file '''
        if self.__logFile is not None:
            self.__logFile.write("\n")
            self.__logFile.close()
            self.__isLogFileOpen = self.__isLogToFile = False
        
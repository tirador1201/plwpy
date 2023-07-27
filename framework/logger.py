import logging


class Logger:
    '''
    Supposed to be custom logger
    '''
    def __init__(self):
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)


    def info(self, msg, *args, **kwargs):
        self.log.info(msg, *args, **kwargs)


clogger = Logger()


def log_text(log_message, *args, **kwargs):
    '''
    Logs info message
    :param log_message: main text
    :param args: possible format parameters
    :param kwargs: keyword params (e.g if necessary to pass the exception)
    :return:
    '''
    clogger.info(log_message, *args, **kwargs)

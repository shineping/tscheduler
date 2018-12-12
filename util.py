import logging
def get_logger(logname,log_path):
    logger = logging.getLogger(logname)
    logger.setLevel(logging.INFO)
    hanlder = logging.FileHandler(log_path)
    formater = logging.Formatter('%(asctime)s:%(module)s %(message)s',datefmt='%Y/%m/%d:%H-%M-%S')
    hanlder.setFormatter(formater)
    hanlder.setLevel(logging.INFO)
    logger.addHandler(hanlder)
    logger.propagate = False
    return  logger
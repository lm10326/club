#coding=utf-8
import logging
def log(message):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    fh = logging.FileHandler(r'D:\test.log')
    formatter = logging.Formatter('%(asctime)s - %(filename)s -%(name)s- [line:%(lineno)d]- %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.info(message)

    # return logger.debug(message)

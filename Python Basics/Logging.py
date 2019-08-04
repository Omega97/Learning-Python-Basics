import logging


# create ad configure logger
logging.basicConfig(filename='log.log', level=logging.DEBUG)
logger = logging.getLogger()

# test the logger
logger.info('message')

print(logger.level)

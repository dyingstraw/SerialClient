import logging
logging.basicConfig(level = logging.INFO,format = '%(lineno)d Lines: %(threadName)s-%(thread)d, %(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log(msg):
    logger.info(msg)
from log import Logger

logger = Logger("file1.txt")

logger.info('Log message - imported')
logger.critical('This is a critical message.')
logger.warning('A warning')
logger.error('And this is an error.')

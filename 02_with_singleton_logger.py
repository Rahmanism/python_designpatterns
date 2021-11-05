from singleton_logger import SingletonLogger

logger1 = SingletonLogger('f1.txt')
# logger1.file_name = 'f1.txt'
logger1.critical('test for f1 from logger1')

logger2 = SingletonLogger('f23.txt')
logger2.file_name = 'f2.txt'
logger2.warning('warning for f2 from logger2')

logger1.error('is this in f2 from logger1?')


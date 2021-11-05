def Singleton(cls):
  instances={}

  def getInstance(*args, **kwargs):
    if cls not in instances:
      instances[cls] = cls(*args, **kwargs)
    return instances[cls]

  return getInstance

@Singleton
class Logger():
  def __init__(self, file_name):
    self.file_name = file_name

  def _write_log(self, level, msg):
      with open(self.file_name, "a") as log_file:
        log_file.write(f"[{level}] {msg}\n")

  def critical(self, msg):
    self._write_log('CRITICAL', msg)

  def error(self, msg):
    self._write_log('ERROR', msg)

  def warning(self, msg):
    self._write_log('WARNING', msg)

  def info(self, msg):
    self._write_log('INFO', msg)


logger1 = Logger('l1.txt')
# logger1.file_name = 'l1.txt'
logger1.critical('test for f1 from logger1')

logger2 = Logger()
logger2.file_name = 'l2.txt'
logger2.warning('warning for f2 from logger2')

logger1.error('is this in f2 from logger1?')


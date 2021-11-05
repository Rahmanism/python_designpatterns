class SingletonLogger2():
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super().__new__(cls)
    return cls.instance

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


logger1 = SingletonLogger2()
logger1.file_name = 'l1.txt'
logger1.critical('test for f1 from logger1')

logger2 = SingletonLogger2()
logger2.file_name = 'l2.txt'
logger2.warning('warning for f2 from logger2')

logger1.error('is this in f2 from logger1?')


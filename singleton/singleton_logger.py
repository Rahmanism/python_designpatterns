class SingletonLogger(object):
  class __SingletonLogger():
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

  instance = None

  def __new__(cls, file_name):
    if not SingletonLogger.instance:
      SingletonLogger.instance = SingletonLogger.__SingletonLogger(file_name)
    return SingletonLogger.instance

  def __getattribute__(self, name):
    return getattr(self.instance, name)

  def __setattr__(self, name, value):
    return setattr(self.instance, name, value)

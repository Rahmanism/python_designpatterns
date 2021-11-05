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


class SingletonObject(object):
  class __SingletonObject():
    def __init__(self):
      self.val = None

    def __str__(self):
      return f"{self!r} {self.val}"

  instance = None

  def __new__(cls):
    if not SingletonObject.instance:
      SingletonObject.instance = SingletonObject.__SingletonObject()
    return SingletonObject.instance

  def __getattribute__(self, name):
    return getattr(self.instance, name)

  def __setattr__(self, name, value):
    return setattr(self.instance, name, value)

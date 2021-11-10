class Book:
  _shared_state = {'1': '2', 'y': 10}
  def __init__(self):
    self.x = 150
    self.__dict__ = self._shared_state
    pass

b1 = Book()
b2 = Book()
b1.x = 200
b2.y = '000'

print('Book obj "b1": ', b1)
print('Book obj "b2": ', b2)
print('obj state "b1": ', b1.__dict__)
print('obj state "b2": ', b2.__dict__)

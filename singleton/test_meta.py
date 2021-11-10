class Meta1():
  a = 'A'
  def __init__(self, x):
    self.x = x
  
m1 = Meta1(5)

class Meta2(Meta1):
  def __init__(self, x, y):
    super().__init__(x)
    self.y = y

m2 = Meta2(1,2)
m2.a = 'B'

print(m1.x, m1.a)
print(m2.a, m2.x, m2.y)

print(type(Meta1))
print(type(Meta2))

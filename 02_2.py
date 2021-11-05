from singleton_object import SingletonObject

obj1 = SingletonObject()
obj1.val = "VALUE 1"
print('obj1: ', obj1)

obj2 = SingletonObject()
obj2.val = "VALUE 2"
print('obj1: ', obj1)
print('obj2: ', obj2)

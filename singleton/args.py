def test_args(arg1, *args, **kargs):
  print('First arg: ', arg1)
  for a in args:
    print('Argument: ', a)
  if kargs is not None:
    for ka, kav in kargs.items():
      print(f"{ka}: {kav}")
  else:
    print('no kargs')

test_args('f', 1,5,'ff','ss', x=5 )
test_args('r',x=5)

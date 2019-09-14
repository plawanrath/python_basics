# kwargs
def test(**kwargs):
  for k, v in kwargs.items():
    print ("%s %s" %(k, v))

print ("**kwargs example")
test(a=1, b=2)

#kwargs without the keyword works too
def test2(**args):
  for k, v in args.items():
    print ("%s %s" %(k, v))

print ("Without using kwargs as function parameter name")
test2(a=1, b=2)

#Call function with kwargs with a dictionary
print ("Pass a dictionary as **args")
d = {'a': 1, 'b': 2, 'c': 3}
test2(**d)

# Passing list as args
def test3(*args):
  for v in args:
    print (v)

l = [1, 2, 3, 4, 5]
print ("Passing list as *args")
test3(*l)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#skd
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#rtj
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#ghsh
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
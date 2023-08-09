a=input("a= ")
b=input("b= ")
def raise_exception():
    add=a/b
    return add
try:
   raise_exception()
   if type(a)==str:
       raise TypeError
except TypeError as te:
    print ("exception raised")

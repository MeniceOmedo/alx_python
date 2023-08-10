def raise_exception_msg(message=""):
    a=3
    b=5
    add=a+b+c
    return add
try:
    raise_exception_msg("c is fun")
    
except NameError as ne:
    print(ne)    
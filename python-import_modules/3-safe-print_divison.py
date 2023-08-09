a=int(input("a= "))
b=int(input("b= "))
def safe_print_division(a,b):
    division=a/b
    return division
try:
    safe_print_division(a,b)

except Exception:
    result=None
    print("inside result: {}".format(result))
    print("{:d} / {:d} = {}".format(a,b,result))
finally:
    if b!=0:
      result=safe_print_division(a,b)
      print("inside result: {}".format(result))
      print("{:d} / {:d} = {}".format(a,b,result))  
    

    




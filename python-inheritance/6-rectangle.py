from base_geometry_5 import BaseGeometry
class Rectangle(BaseGeometry):
    """The class Rectangle inherits from the class BaseGeometry
    Args:
        width(int):a private instance variable taken as the first parameter
        height(int): a private instance variable taken as the second parameter
    """
    def __init__(self,width,height):
        self.__width=width
        self.__height=height
        self.integer_validator(self.__width,self.__height)

r=Rectangle(3,5)        
#print(r)  
#print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width,r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__,e))

try:
    r2=Rectangle(4,True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__,e))    

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
        self.w=self.__width
        self.h=self.__height
    def __str__(self):
        """The str() can now be used once we have the __str__ method"""
        return ("[Rectangle] {}/{}".format(self.__width,self.__height))    


r=Rectangle(3,5)

print(r)
print(r.area())

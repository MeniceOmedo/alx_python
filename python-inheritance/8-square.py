from rectangle_7 import Rectangle
class Square(Rectangle):
    """The class Square inherits from the class Rectangle
    Args:
      size(int): a private instance variable
    """
    def __init__(self,size):
        self.__size=size
        self.integer_validator(self.__size,self.__size)
        self.w=self.__size
        self.h=self.__size

    def __str__(self):
        """ the str function can be used once we have the __str__ method"""
        return ("[Rectangle] {}/{}".format(self.__size,self.__size))     

s=Square(13) 

print(s)
print(s.area())


        
    
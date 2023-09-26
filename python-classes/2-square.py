class Square:
    """ The class square fundamentally is created 
    Args:
      size(int):a private class attribute
    Exception:
       an exception is raised when size is not an integer
       an exception is raised when size is less than or equal to 0
    """
    def __init__(self,size=0):
        
        self.__size=size
        if type(self.__size )!= int:
            raise Exception ("size must be an integer")
        if self.__size<0:
            raise Exception ("size must be >= 0")
    def area(self):
        ara=self.__size**2
        return ara
    
        
# we create the first instance of a square with a width of 3
my_square_1=Square(3)   
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:

    """ try command is needed to eliminate occurances of errors ,
    that are assumed to arise when executing the program
    """
    print(my_square_1.__size)
except Exception as e:
     #we can use a general exception format  to catch any unspecified or specified errors for this case
    print(e)  



# we create the second instance of a square with a width of 3
my_square_2=Square(5)
print("Area: {}".format(my_square_2.area()))
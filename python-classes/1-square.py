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
              
# we create the first instance of a square with a width of 3    
my_square_1=Square(3)

print(type(my_square_1))
print(my_square_1.__dict__)


my_square_2=Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:

    """ try command is needed to eliminate occurances of errors ,
    that are assumed to arise when executing the program
    """

    print(my_square_1.size)
except Exception as e:
     #we can use a general exception format  to catch any unspecified or specified errors for this case
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
#we can use a general exception format  to catch any unspecified or specified errors for this caset Exception as e:

    print(e)  



try:
    """To ensure that our error handling is working we carry out such a run by using an input that
    is expected to give an error

    """
    my_square_3=Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    """The value -89 is inputed to test the working of 
    the program.
    """
    my_square_4=Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)      
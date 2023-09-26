class Square:


    """ The class square fundamentally is created 
    Args: 
       size(int): a private class variable
    """


    def __init__(self,size):
        
        self.__size=size

# we create the first instance of a square with a width of 3
my_square=Square(3)
# the type function serves to let us know if the object my_square is indeed an instance of the
#class Square
print(type(my_square))

print(my_square.__dict__)

try:
    """ try command is needed to eliminate occurances of errors ,
    that are assumed to arise when executing the program
    """
    print(my_square.size)
except Exception as e:
    #we can use a general exception format  to catch any unspecified or specified errors for this case
    print(e)

try:
    print(my_square.__size)
except Exception as e:
     #we can use a general exception format  to catch any unspecified or specified errors for this case
    print(e)  
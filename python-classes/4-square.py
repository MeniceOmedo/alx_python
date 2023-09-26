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
        if self.__size <0:
               raise Exception ("size must >= 0")
             
    def area(self):
        """A public class method
        Returns:
          returns the area of a figure
        """
        ara=self.__size**2
        return ara
    @property
    def size(self):
        """the getter method access the private variable size"""
        return self.__size
    @size.setter
    def size(self,value):
        try:

            
            """ try command is needed to eliminate occurances of errors ,
    that are assumed to arise when executing the program
    """ 
            self.__size=value
            if type(self.__size )!= int:
               raise Exception ("size must be an integer")
            if self.__size <0:
               raise Exception ("size must be >= 0")
            
        except ValueError as e:
            print(e)
            
        except TypeError as e:
            print(e)


    def my_print(self):
        if self.__size==0:
            print()
        else:
            for n in range(self.__size):
                for k in range(self.__size):
                    print("#",end=" ")
                print()

                
        


# we create the first instance of a square with a width of 3
my_square=Square(3)
my_square.my_print()


print("--")
# we create the second instance of a square with a width of 3
my_square=Square(10)
my_square.my_print()


print("--")

# we create the third instance of a square with a width of 3
my_square=Square(0)
my_square.my_print()


print("--")
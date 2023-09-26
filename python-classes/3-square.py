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
            self.__size=value
            if type(self.__size )!= int:
               raise Exception ("size must be an integer")
            if self.__size <0:
               raise Exception ("size must be >= 0")
            
        except ValueError as e:
            print(e)
            
        except TypeError as e:
            print(e)
            
            
        
            
           
    
# we create the first instance of a square with a width of 3
my_square=Square(89)   
print("Area: {} for size: {}".format(my_square.area(),my_square.size)) 



# we create the second instance of a square with a width of 3
my_square.size=3
print("Area: {} for size: {}".format(my_square.area(),my_square.size)) 


try:

    """ try command is needed to eliminate occurances of errors ,
    that are assumed to arise when executing the program
    """
    my_square.size="5 feet"
    print("Area: {} for size: {}".format(my_square.area(),my_square.size)) 

except Exception as e:
     #we can use a general exception format  to catch any unspecified or specified errors for this case
    print(e)
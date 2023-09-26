class BaseGeometry:
    
    def area(self):
        """A public class method
        Args:
          it takes no arguments
        Returns:
           the try command raises an exception when an error is encountered
        """
        try:
           ara=self.w*self.h  
           return ara 
        except Exception:
          raise Exception ("area() is not implemented")
    
    def integer_validator(self,name,value):
          """The public class method
          Args:
              name(str):first parameter
              value(int):second parameter
          Returns:
              the try command raises a TypeError when the value argument is not an integer
              the try command raises a ValueError when the value argument is less than 0
          """
        
          if (type(value)) != int:
            raise TypeError ("{} must be an integer".format(name))
          elif value<=0:
            raise ValueError ("{} must be greater than 0".format(name))
          
    

bg=BaseGeometry()
bg.integer_validator("my_int",12)
bg.integer_validator("width",89)

try:
   bg.integer_validator("name","john")
except Exception as e:
   print("[{}] {}".format(e.__class__.__name__,e))


try:
   bg.integer_validator("age",0)
except Exception as e:
   print("[{}] {}".format(e.__class__.__name__,e))


try:
   bg.integer_validator("distance",-4)
except Exception as e:
   print("[{}] {}".format(e.__class__.__name__,e))   
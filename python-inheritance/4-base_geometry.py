#!/usr/bin/python3
class BaseGeometry:
    
    """The class BaseGeometry
    """
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
    

bg=BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__,e))

from base_geometry_5 import BaseGeometry
class Rectangle(BaseGeometry):
    def __init__(self,width,height):
        self.__width=width
        self.__height=height
        self.integer_validator(self.__width,self.__height)
        self.w=self.__width
        self.h=self.__height
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width,self.__height))    

if __name__=="__main__":
  r=Rectangle(3,5)

  print(r)
  print(r.area())

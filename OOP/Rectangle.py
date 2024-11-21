class Rectangle:
    def __init__(self,width:int=1, height:int=1)->None:
        self.width=width
        self.height=height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value)->None:
        if not value:
           raise ValueError("Please define valid value")
        if value>0:
           if isinstance(value, int) or isinstance(value,float):
              self.__width=value
           else:
              raise ValueError("Not valid width") 
        else:
            raise ValueError("Not valid width")

        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value)->None:
        if not value:
           raise ValueError("Please define valid value")
        if value>0:
           if isinstance(value, int) or isinstance(value,float):
              self.__height=value
           else:
              raise ValueError("Not valid height") 
        else: 
           raise ValueError("Not valid height")
    
    @property
    def area(self):
        """ Calculates the area"""
        return self.height * self.width
    
    @property
    def perimeter(self):
        """ Calculates the perimeter """
        return 2*(self.height + self.width)
    

def main():
   
    w=5
    h=4
    #h=-4
    
    r1=Rectangle(w,h)
    print(f"Rectangle with  height: {r1.height},width: {r1.width}")
    print(f"Area: {r1.area}")
    print(f"Perimeter: {r1.perimeter}")
    
if __name__=="__main__":
    main()

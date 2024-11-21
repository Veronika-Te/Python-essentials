import math

def find_area_circle(**kwargs)->float: 
    """Finds area of circle"""
    if not kwargs:
        return 0
    r=kwargs['radius']
    return (math.pi) * r**2

def find_area_triangle(**kwargs)->float:
    """Finds area of triangle"""
    if not kwargs:
        return 0
    base=kwargs['base']
    height=kwargs['height']    
    return 1/2*base*height

def find_area_square(**kwargs)->float :  
    """Finds area of square"""
    if not kwargs:
        return 0
    side=kwargs['side']
    return side**2

def find_area_rectangle(**kwargs)->float:
    """Finds area of rectangle"""
    if not kwargs:
        return 0
    length=kwargs['length']
    width=kwargs['width']
    return length*width



def calculate_area(shape:str, **kwargs)->float:
    """Uses dictionary of functions to calculate the area based on the provided shape and parameters."""
    
    find_areas={'Circle':find_area_circle, 'Triangle':find_area_triangle, 'Square': find_area_square, 'Rectangle':find_area_rectangle}
    shapes={'Circle', 'Triangle','Square',  'Rectangle'}
    if not shape or not kwargs:
       return 0 
    if shape in shapes:
        if shape=='Circle':
           circle=find_areas.get('Circle')
           area=circle(**kwargs)
           return area
        elif shape=='Triangle':
           triangle=find_areas.get('Triangle')
           area=triangle(**kwargs)
           return area
        elif shape=='Square':
           square=find_areas.get('Square')
           area=square(**kwargs)
           return area 
        elif shape=='Rectangle':
           rectangle=find_areas.get('Rectangle')
           area=rectangle(**kwargs)
           return area
        else:
            return 0
        
    else:
        return 0

def main()->None:
   
   print("Calculating areas of different shapes")
   #Circle
   r=5
   circle_area=calculate_area('Circle',radius=r)
   print("Circle area")
   print(circle_area)
   print("\n")
   #Triangle
   b=5
   h=7
   triangle_area=calculate_area('Triangle',base=b,height=h) 
   print("Triangle area")
   print(triangle_area)
   print("\n")
   #Square
   side_square=7
   square_area=calculate_area('Square',side=side_square)
   print("Square area")
   print(square_area)
   print("\n")
   #Rectangle
   l=7
   w=8
   rectangle_area=calculate_area('Rectangle', length=l,width=8)
   print("Rectangle area")
   print(rectangle_area)
   #TODO add user input
   
if __name__=="__main__":
    main()


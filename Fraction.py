from math import gcd
import math
from typing import TypeVar

Fraction=TypeVar("Fraction", bound="Fraction")

class Fraction:
    
    def __init__(self, numerator:int, denominator:int):
        self.setNumerator(numerator)
        self.setDenominator(denominator)
        self.simplifyFraction()
        self._is_hashed = False  # Track if the object has been hashed
    
    def getNumerator(self):
        return self.__numerator
    
    def setNumerator(self, numerator):
        if numerator is None:
           raise ValueError("Not valid numerator")
        if numerator==0: 
           self.__numerator=0
        if isinstance(numerator,int):
           self.__numerator=numerator
        
    def getDenominator(self):
        return self.__denominator
        
    def setDenominator(self, denominator):
        if not denominator:
           raise ValueError("Not valid denominator")
        if denominator == 0:
           raise ZeroDivisionError("Denominator cannot be zero.")
        if isinstance(denominator, int):
            self.__denominator=denominator
        else:
            raise ValueError("Not valid denominator")
        
    #String represantions
    def __str__(self)-> str:
        """Returns a user-friendly string representation"""
        if self.isNull():
           return "0"
        return f"{self.getNumerator()}/{self.getDenominator()}"
    
    def __repr__(self) -> str:
        """Returns an unambiguous string representation suitable for debugging"""
        return f"{self.__class__.__name__} ({self.getNumerator()!r}/{self.getDenominator()!r}) ".format(self)
    
    #Simplify
    def simplifyFraction(self)->None:
        """Simplifies fraction"""
        if not self.isNull():
           numerator=self.getNumerator()
           denominator=self.getDenominator()
           common_divisor=gcd(numerator, denominator)
        
           numerator //=common_divisor
           self.setNumerator(numerator)
           denominator //=common_divisor
           self.setDenominator(denominator)
        
    
    def isNull(self):
        """Checks if numerator is 0"""
        if self.getNumerator()==0:
            return True
        return False
    
    #Arithmetic Operations   
    def __add__(self,other)->Fraction:
        """Returns result of addition."""
        if not other:
           return Fraction(self.getNumerator(), self.getDenominator()) 
        if isinstance(other, Fraction):
           new_numerator=(self.getNumerator() * other.getDenominator()) + (other.getNumerator() * self.getDenominator())
           new_denominator=self.getDenominator()*other.getDenominator()
           return Fraction(new_numerator,new_denominator)
        elif isinstance(other, int):
           new_Fraction=Fraction(other, 1)
           new_numerator=(self.getNumerator() * new_Fraction.getDenominator()) + (new_Fraction.getNumerator() * self.getDenominator())
           new_denominator=self.getDenominator()*new_Fraction.getDenominator()
           return Fraction(new_numerator,new_denominator)
        else:
            raise ValueError ("Not valid value to add")
           
    def __sub__(self, other):
        """Returns result of subtraction"""
        if not other:
           return Fraction(self.getNumerator(), self.getDenominator()) 
        if isinstance(other, Fraction):
           new_numerator = (self.getNumerator() * other.getDenominator()) - (other.getNumerator() * self.getDenominator())
           new_denominator = self.getDenominator() * other.getDenominator()
           return Fraction(new_numerator, new_denominator)   
        elif isinstance(other, int):  
           new_Fraction=Fraction(other, 1)
           new_numerator=(self.getNumerator() * new_Fraction.getDenominator()) - (new_Fraction.getNumerator() * self.getDenominator())
           new_denominator=self.getDenominator()*new_Fraction.getDenominator()
           return Fraction(new_numerator,new_denominator)
        else:
            raise ValueError ("Not valid value to substract")

    def __mul__(self,other)-> Fraction:
        """Returns result of multipication. Fraction type multiply with Fraction type or integer type"""
        if isinstance(other, Fraction):
           new_numerator=self.getNumerator() * other.getNumerator()
           new_denominator=self.getDenominator() * other.getDenominator()
           return Fraction(new_numerator,new_denominator)
        elif isinstance(other, int):
           new_numerator=self.getNumerator() * other
           return Fraction(new_numerator,self.getDenominator())
        elif other==0:
           return 0 
        else:
            raise ValueError("Not valid multiplier")
     
    def __truediv__(self, other):
        """Returns result of division."""
        if not other:
           raise ValueError("Not valid divider")
        elif isinstance(other, Fraction):
           new_numerator = self.getNumerator() * other.getDenominator()
           new_denominator = self.getDenominator() * other.getNumerator()
           return Fraction(new_numerator, new_denominator) 
        elif isinstance(other, int):
           new_denominator=self.getDenominator() * other
           return Fraction(self.getNumerator(), new_denominator) 
        else:
            raise ValueError("Not valid divider")
        
    #Rich Comparison Methods
    #Equal
    def __eq__(self,other):
        """Evaluates the equality of two objects"""
        if not other:
           return False
        if self.isNull():
           if other is None:
               return True
           else:
               return False
        if isinstance(other, Fraction):
           if self.getNumerator()==other.getNumerator() and self.getDenominator()==other.getDenominator():
              return True
        else:
            return False
    #Not equal
    def __ne__(self, other)-> bool:
        """Checks if two types are not equal"""
        if not other:
           return True
        if type(other) != type(self):
           return True
        if self.isNull() and other is None:
            return False
        else:
            if (self.getNumerator() != other.getNumerator()):
                return True
            elif self.getDenominator() != other.getDenominator():
                return True
            else:
                return False
            
   
        
#     #TODO
# """Less than: __lt__(self, other)
    def __lt__(self, other)->bool:
        if not other:
            return False
        if isinstance(other, Fraction):
            if self.getDenominator()==other.getDenominator():
               if self.getNumerator() < other.getNumerator():
                   return True
               else:
                   return False
            else:
                if (self.getNumerator() * other.getDenominator()) < (other.getNumerator()*self.getDenominator()):
                   return True
                else:
                   return False
        elif isinstance(other, int):
            new_denominator=1
            new_fraction=Fraction(other, new_denominator) #creating Fraction with denominator =1
            if (self.getNumerator() * new_fraction.getDenominator()) < (new_fraction.getNumerator()*self.getDenominator()):
                return True
            else:   
                return False
        else:
            raise ValueError("Given value is Invalid for comparison with Fraction")
        
# Less than or equal to: __le__(self, other)
# Greater than: __gt__(self, other)
# Greater than or equal to: __ge__(self, other)"""        
    #Hashing
    def __hash__ (self)->int:
        """ Extracts Hash code to allow fractions to be used in sets and as dictionary keys."""
        n=self.getNumerator()
        d=self.getDenominator()
        if self.isNull():
           return 0 
        #check if was hashed in the past or not 
        if not self._is_hashed:
           self._is_hashed=True # Track if the object has been hashed
        return hash((n,d)) 
    
    #Additional Methods
    def __float__(self) ->float:
        """Casts fraction to float"""
        if self.isNull():
           return 0
        fl_fraction=float(self.getNumerator()) / (self.getDenominator())
        return fl_fraction                                          
        
    def __int__(self)->int:
        """Casts fraction to int"""
        if self.isNull():
           return 0
        int_fraction=math.trunc((self.getNumerator()) / (self.getDenominator()))
        return int_fraction
        
    #Implement __neg__ for unary negation (e.g., -fraction)."""
    def __neg__(self)->Fraction:
        if self.isNull():
           return 0
        return Fraction(-self.getNumerator(), self.getDenominator())
    
    #Optional Advanced Features
    
    #Inplace operations
    def __iadd__(self,other):
        """Supporting += """
        if not other:
           return self
        if isinstance(other, Fraction):
           new_numerator=self.getNumerator() * other.getDenominator() + other.getNumerator() * self.getDenominator()
           self.setNumerator(new_numerator)
           new_denominator=self.getDenominator()*other.getDenominator()
           self.setDenominator(new_denominator)
           self.simplifyFraction()
           return self
        elif isinstance (other, int):
           new_numerator=self.getNumerator() * 1 + other * self.getDenominator()
           self.setNumerator(new_numerator)
           self.simplifyFraction()
           return self
        else:
            raise ValueError("Not valid operand")
      
    
    def __isub__(self,other):
        """Supporting -= """
        if not other:
           return self
        if isinstance(other, Fraction):
           new_numerator = (self.getNumerator() * other.getDenominator()) - (other.getNumerator() * self.getDenominator())
           self.setNumerator(new_numerator)
           new_denominator = self.getDenominator() * other.getDenominator()
           self.setDenominator(new_denominator)
           self.simplifyFraction()
           return self
        elif isinstance (other, int):
           new_numerator=self.getNumerator() * 1 - other * self.getDenominator()
           self.setNumerator(new_numerator)
           self.simplifyFraction()
           return self
        else:
            raise ValueError("Not valid operand")
       
# TODO:
# Optional Advanced Features    
# Immutability
# Use @dataclass(frozen=True) from the dataclasses module to make Fraction instances immutable.

# Augmented Assignment
# Support augmented assignment operations (e.g., fraction1 += fraction2).

class MixedFraction(Fraction):
     def __init__(self, numerator:int, denominator:int, whole_part:int ):
         super().__init__(numerator,denominator)
         self.__whole_part=whole_part
         
     def getWholePart(self):
         return self.__whole_part
     
     def setWholePart(self, wh_part):
         if not wh_part:
             raise ValueError("Invalid whole part")
         if isinstance(wh_part,int):
            self.__whole_part=wh_part
         else:
             raise ValueError("Invalid whole part")
     
     def __str__(self):
         return f"{self.__whole_part} {self.getNumerator()}/{self.getDenominator()}"




def main()->None:
    print("-----------------Fractions-----------------")
    
    print("--------------String Representation--------------")
    f1= Fraction(1,7)
    print(f"__str__ : {str(f1)}")
    print(f"__repr__: {repr(f1)}")
    
    # f1.simplifyFraction()
    # print(str(f1))
    f2 = Fraction(3,7)
    


    print("--------------Arithmetic Operations---------")
    #Addition
    print("\nAddition")
    i=5
    print(f"{str(f1)} + {str(f2)} = {f1+f2}")
    print(f"{str(f1)} + {i} = {f1+i}")
    
    #Subtraction
    print("\nSubtraction")
    i=5
    print(f"{str(f1)} - {str(f2)} = {f1-f2}")
    print(f"{str(f1)} - {i} = {f1-i}")

    #Multiplication
    print("\nMultiplication")
    print(f"{str(f1)} * {str(f2)} =  {f1*f2}")
    m2=4
    res=f1*m2
    print(f"{str(f1)} * {m2} =  {res}")
    
    #Division
    print("\nDivision")
    print(f"{str(f1)} / {str(f2)} =  {f1/f2}")
    


    print("\n--------------Rich comparisons--------------")
    print("\nEquality")
    #equality    
    if f1==f2:
       print(f"True,{str(f1)} equal to {str(f2)}")
    else:
       print(f"False,{str(f1)} are not equal to {str(f2)}")
        
    #not equal
    if f1!=f2:
       print(f"True,{str(f1)} are not equal to {str(f2)}")
    else:
       print(f"False,{str(f1)} equal to {str(f2)}")    
       
    #Comparison
    print("Less than")
    if f1<f2:
        print(f"TRUE: {f1}<{f2}")
    else:
        print (f"FALSE: {f1}<{f2}")
       
    print("Checking Greater than(>)")
    print(f" {f1}>{f2} => {f1>f2}")
    
    print(f1<f1)
    

    print("--------------Hashing Support--------------") 
    print("\nHashing")
    #Hashing
    print(f"f1: {repr(f1)} ")
    
    print(f"Hash code for fraction {f1} : {(hash(f1))}")
    #Ensure that equivalent fractions have the same hash value.
    #Checking..
    f3=Fraction(2,7)
    print(f"f3: {repr(f3)}")
    print(f"Hash code for fraction {f3} : {(hash(f3))}")
    if hash(f1)==hash(f3):
        print("Equivalent fractions have the same hash value.")
        
    print("\n--------------Additional methods--------------")
    
    #Cast to float
    f4=Fraction(89,7) 
    
    print(f"Cast to float {float(f4)}")
    #Cast to int(truncate)
    print(f"Conversion to integer (truncating towards zero): {int(f4)}")
    #Unary negation
    print(f"UnaryNegation: {-f4}")
    

    #+=
    print("in-place arithmetic methods ")
    print(str(f1))
    print("\nCheck iadd")
    f1+=f2
    print(f"{f1} += {f2}")
    print(f"{f1}")
    
    print("iadd with int")
    #print(f"{f1}")
    x=7
    f1+=x
    print(f1)
    #-=
    print("\nCheck isub")
    f1-=f2
    print(f1)
    
    print("isub with int")
    x=7
    f1-=x
    print(f1)

    #Creating mixed fraction
    mx_f=MixedFraction(1,2,4)
    print("\nMixed Fraction")
    print(str(mx_f))

        


if __name__ == "__main__":
   main()
            
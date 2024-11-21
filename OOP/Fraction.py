from math import gcd
import math
from typing import TypeVar
Fraction=TypeVar("Fraction", bound="Fraction")

class Fraction:
    def __init__(self, numerator:int, denominator:int)->None:
        self.setNumerator(numerator)
        self.setDenominator(denominator)
        self.simplifyFraction()
        self._is_hashed = False  # Track if the object has been hashed
    
    def getNumerator(self)->int:
        return self.__numerator
    
    def setNumerator(self, numerator:int)->None:
        if numerator is None:
           raise ValueError("Not valid numerator")
        if numerator==0: 
           self.__numerator=0
        if isinstance(numerator,int):
           self.__numerator=numerator
        
    def getDenominator(self)->int:
        return self.__denominator
        
    def setDenominator(self, denominator: int)->None:
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
        
    
    def isNull(self)->bool:
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
           new_numerator=self.getNumerator() + (other * self.getDenominator())
           new_denominator=self.getDenominator()
           return Fraction(new_numerator,new_denominator)
        else:
            raise TypeError ("Not valid value to add")
           
    def __sub__(self, other)->Fraction:
        """Returns result of subtraction"""
        if not other:
           return Fraction(self.getNumerator(), self.getDenominator()) 
        if isinstance(other, Fraction):
           new_numerator = (self.getNumerator() * other.getDenominator()) - (other.getNumerator() * self.getDenominator())
           new_denominator = self.getDenominator() * other.getDenominator()
           return Fraction(new_numerator, new_denominator)   
        elif isinstance(other, int): 
           new_numerator=self.getNumerator() - (other * self.getDenominator())
           new_denominator=self.getDenominator()
           return Fraction(new_numerator,new_denominator)
        else:
            raise TypeError ("Not valid value to substract")

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
            raise TypeError("Not valid multiplier")
     
    def __truediv__(self, other)->Fraction:
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
            raise TypeError("Not valid divider")
        
    #Rich Comparison Methods
    #Equal
    def __eq__(self,other)->bool:
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

    def __lt__(self, other)->bool:
        """Checks if the given fraction is less than another fraction (or integer)"""
        if not other:
           return False
        if self.isNull():
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
            return False
        else:
            raise TypeError("Given value is Invalid for comparison with Fraction")

    def __gt__(self,other)->bool:
        """Checks if the given fraction is greater than another fraction (or integer)"""
        if not other:
           return False
        if self.isNull():
           return False 
        if isinstance(other, Fraction):
            if self.getDenominator()==other.getDenominator():
               if self.getNumerator() > other.getNumerator():
                   return True
               else:
                   return False
            else:
                if (self.getNumerator() * other.getDenominator()) > (other.getNumerator()*self.getDenominator()):
                   return True
                return False
        elif isinstance(other, int):
            new_denominator=1
            new_fraction=Fraction(other, new_denominator) #creating Fraction with denominator =1
            if (self.getNumerator() * new_fraction.getDenominator()) > (new_fraction.getNumerator()*self.getDenominator()):
                return True
            return False
        else:
            raise TypeError("Given value is Invalid for comparison with Fraction")
    
         
    def __le__(self, other)->bool:
        """Checks if the given fraction is less than or equal to another fraction (or integer)"""
        if not other:
           return False
        if self.isNull():
           return False 
        if isinstance(other, Fraction):
           # Compare two fractions
           left_side = self.getNumerator() * other.getDenominator()
           right_side = other.getNumerator() * self.getDenominator()
           return left_side <= right_side
        elif isinstance(other, int):
            denominator=1
            left_side = self.getNumerator() * denominator
            right_side = other * self.getDenominator()
            return left_side <= right_side
        else:
           raise TypeError("Given value is Invalid for comparison with Fraction")
       
    
    def __ge__(self,other)->bool:
        """Checks if the given fraction is greater than or equal to another fraction (or integer)"""
        if not other:
           return False
        if self.isNull():
           return False 
        if isinstance(other, Fraction):
           # Compare two fractions
           left_side = self.getNumerator() * other.getDenominator()
           right_side = other.getNumerator() * self.getDenominator()
           return left_side >= right_side
        elif isinstance(other, int):
            denominator=1
            left_side = self.getNumerator() * denominator
            right_side = other * self.getDenominator()
            return left_side >= right_side
        else:
           raise TypeError("Given value is Invalid for comparison with Fraction")
        
            
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
        

    def __neg__(self)->Fraction:
        """Unary negation (e.g., -fraction)."""
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
           new_numerator=self.getNumerator()+ other * self.getDenominator()
           self.setNumerator(new_numerator)
           self.simplifyFraction()
           return self
        else:
            raise TypeError("Not valid operand")
    
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
            raise TypeError("Not valid operand")
       
# TODO:
# Augmented Assignment
# Support augmented assignment operations (e.g., fraction1 += fraction2).?

class MixedFraction(Fraction):
     def __init__(self, numerator:int, denominator:int, whole_part:int )->None:
         super().__init__(numerator,denominator)
         self.__whole_part=whole_part
         
     def getWholePart(self)->int:
         return self.__whole_part
     
     def setWholePart(self, wh_part)->None:
         if not wh_part:
             raise ValueError("Invalid whole part")
         if isinstance(wh_part,int):
            self.__whole_part=wh_part
         else:
             raise TypeError("Invalid whole part")
     
     def __str__(self)->str:
         return f"{self.__whole_part} {self.getNumerator()}/{self.getDenominator()}"



#Functions for printing, which will be called in main function
def print_and_check_arithmetic_operations(f1,f2)->None:
    """Prints and checks arithmetic operations"""
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
    
def print_and_check_rich_comparisons(f1,f2,f7):
    """Prints and checks rich comparisons"""
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
    print("\nChecking Less than(<)")
    
    check_int=7
    print(f"{f1}<{f2}=>{f1<f2}") 
    print(f"{f7}<{f2}=>{f7<f2}")

    print("\nChecking Greater than(>)")
    print(f" {f1}>{f2} => {f1>f2}")
    
    print("\nChecking less than or equal to (<=)")
    print(f"{f1}<={f2}=> {f1<=f2}")
    print(f"{f1}<={check_int}=>{f1<=f2}")
    print(f"{f1}<={f1}=>{f1<=f1}")
    
    print("\nChecking greater than or equal to(>=)")
    print(f"{f1}>={f2}=> {f1>=f2}")
    print(f"{f1}>={check_int}=>{f1>=f2}")
    print(f"{f1}>={f1}=>{f1>=f1}")

def print_and_check_hashing(f1,f3)->None:
    """Prints and checks hashing"""
    print("\n--------------Hashing Support--------------") 
    print("\nHashing")
    #Hashing
    print(f"f1: {repr(f1)} ")
    print(f"Hash code for fraction {f1} : {(hash(f1))}")
    #Ensure that equivalent fractions have the same hash value.
    #Checking..
    
    print(f"f3: {repr(f3)}")
    print(f"Hash code for fraction {f3} : {(hash(f3))}")
    if hash(f1)==hash(f3):
        print("Equivalent fractions have the same hash value.")
        
def print_and_check_additionalmethods(f4)->None:
    """Prints and checks additional methods"""
    print("\n--------------Additional methods--------------\n")
    #Cast to float
    print(f"Cast to float {float(f4)}")
    #Cast to int(truncate)
    print(f"Conversion to integer (truncating towards zero): {int(f4)}")
    #Unary negation
    print(f"UnaryNegation: {-f4}")
    
def print_and_check_in_place_operations(f1,f2)->None:
    """Prints and checks in-place operations"""
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

        
   


def main()->None:
    print("-----------------Fractions-----------------")
    
    print("--------------String Representation--------------")
    f1= Fraction(1,7)
    print(f"__str__ : {str(f1)}")
    print(f"__repr__: {repr(f1)}")
    
    # f1.simplifyFraction()
    # print(str(f1))
    f2 = Fraction(3,7)
    f3=Fraction(2,7)
    f4=Fraction(89,7) 
    f7=Fraction(0,6)

    #Arithmetic Operations
    print_and_check_arithmetic_operations(f1,f2)
    #Rich comparisons
    print_and_check_rich_comparisons(f1,f2,f7)
    #Hashing Support
    print_and_check_hashing(f1,f3)
    #Additional Methods
    print_and_check_additionalmethods(f4)
    #In-place Operations
    print_and_check_in_place_operations(f1,f2)

    #Creating mixed fraction
    mx_f=MixedFraction(1,2,4)
    print("\n--------------Mixed Fraction--------------")
    print(str(mx_f))

if __name__ == "__main__":
   main()
            
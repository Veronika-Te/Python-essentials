from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Fraction:
    numerator: int
    denominator: int

    def __post_init__(self)->None:
        if self.denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        # Simplifying the fraction
        common_divisor = gcd(self.numerator, self.denominator)
        
        # Since the class is frozen, we need to use object.__setattr__ to modify attributes
        object.__setattr__(self, 'numerator', self.numerator // common_divisor)
        object.__setattr__(self, 'denominator', self.denominator // common_divisor)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
if __name__=="__main__":
   f1=Fraction(5,10) 
   print(f1)

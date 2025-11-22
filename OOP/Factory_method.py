from abc import ABC, abstractmethod

class DeliveryFeeCalculator(ABC):
  @abstractmethod
  def calculate(self, distance: float, base_rate: float = 5.0) -> float:
    pass
  
class FlatRateCalculator(DeliveryFeeCalculator):
  def calculate_fee(self,distance: float, base_rate: float = 5.0) -> float:
      return base_rate  # Flat fee, distance ignored
    
class DistanceBasedCalculator(DeliveryFeeCalculator):
  def calculate_fee(self, distance: float, base_rate: float = 5.0) -> float:
    return base_rate + distance * 2  # Example: $2 per km
  
class SurgePricingCalculator(DeliveryFeeCalculator):
  def __init__(self, surge_multiplier: float):
    self.surge_multiplier = surge_multiplier

  def calculate_fee(self, distance: float, base_rate: float = 5.0) -> float:
    return (base_rate + distance * 2) * self.surge_multiplier
  
class DeliveryFeeFactory:
  @staticmethod
  def create_calculator(calc_type:str, **kwargs) -> DeliveryFeeCalculator:
    if calc_type == "flat":
      return FlatRateCalculator()
    elif calc_type == "distance":
      return DistanceBasedCalculator()
    elif calc_type == "surge":
      surge_multiplier = kwargs.get("surge_multiplier", 1.5)
      return SurgePricingCalculator(surge_multiplier)
    else:
      raise ValueError(f"Unknown calculator type: {calc_type}")
    
if __name__=="__main__":
  # Create a distance-based calculator
  calculator = DeliveryFeeFactory.create_calculator("distance")
  fee = calculator.calculate_fee(distance=10)  # $5 base + 10*2 = $25
  print(fee)

  # Create a surge pricing calculator
  surge_calc = DeliveryFeeFactory.create_calculator("surge", surge_multiplier=2.0)
  print(surge_calc.calculate_fee(distance=10))  # ($5 + 10*2) * 2 = $50
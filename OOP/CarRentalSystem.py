class Car:
  def __init__(self, make, model, speed, rental_price_day):
    self.make=make
    self.model=model
    self.speed=speed
    self.rental_price_day=rental_price_day
    
  def display_details(self):
    """Displays the car's make, model, speed, and rental price."""
    return f"Car's make{self.make}, model {self.model}, speed {self.speed}, rental price: {self.rental_price_day}"
  
  def get_rental_price(self, days):
    """Calculate the total rental price for a specified number of days."""
    if not isinstance(days, int) or not days:
      return "Provide integer number of days"
    print(f"Total sum for rental: {days * self.rental_price_day} $")
    return days * self.rental_price_day
  

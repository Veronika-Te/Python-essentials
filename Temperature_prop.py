class Temperature:
    
    def __init__(self,celsius_temperature: float=0)->None:
        self.celsius_temperature=celsius_temperature
        
    @property
    def celsius_temperature(self)->float:
        return self.__celsius_temperature
    
    @celsius_temperature.setter
    def celsius_temperature(self,value:float)->None:
        min_celsius=-273.15 
        max_celsius=56.7 
        if min_celsius<value<max_celsius:
           if isinstance(value,float) or isinstance(value,int):   
              self.__celsius_temperature=value
           else:
              raise TypeError("Not valid type for temperature")
        else:
           raise ValueError(f"Min Celsius: {min_celsius}°C and Max Celsius: {max_celsius}°C")
        
        
    @property
    def fahrenheit(self)->float:
        # Convert Celsius to Fahrenheit
        return (self.__celsius_temperature * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value:float)->None:
        # Convert Fahrenheit to Celsius
        max_fahren=134.1
        min_fahren=-459.67
        if min_fahren<value<max_fahren:
           if isinstance(value,float) or isinstance(value,int):   
              self.__celsius_temperature = (value - 32) * 5/9
           else:
              raise TypeError("Not valid type for temperature")    
        else:
           raise ValueError(f"Min Fahrenheit {min_fahren}°F and Max Fahrenheit is {max_fahren}°F")

def main()->None:
    #t=70
    t=34
    #temp = Temperature() 
    temp = Temperature(t)  # Initializing with Celsius
    print(f"Temperature in Celsius: {temp.celsius_temperature} °C") 
    print(f"Temperature in Fahrenheit: {temp.fahrenheit} °F")  

if __name__=="__main__":
   main()    
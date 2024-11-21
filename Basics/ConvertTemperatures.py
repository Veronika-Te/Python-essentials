#Converting temperatures between Celsius, Fahrenheit, and Kelvin 
def celsius_to_Farenheit(tmp:float)->float:
    """Converts Celcius temperture to Farenheit using formula: (0 C × 9/5) + 32 = 32 F"""
    if not tmp:
        return 0
    if float(tmp):
       farenheit= (tmp*9/5) +32
       return farenheit
    else: 
       return 0

def celsius_to_Kelvin(tmp:float)->float:
   """Converts Celcius temperture to Kelvin using formula: 0 C + 273,15 = 273,15 K""" 
   if not tmp:
      return 0
   if float(tmp): 
      kelvin=tmp + 273.15
      return kelvin
   else:
      return 0

def farenheit_to_Celsius(tmp:float)->float:
    """Converts Farenheit temperture to Celsius using formula: (32 F − 32) × 5/9 = 0 C"""
    if not tmp:
      return 0
    if float(tmp):  
       celsius=(tmp-32) * (5/9)
       return celsius
    else:
       return 0

def kelvin_to_Celsius(tmp:float)->float:
    """Converts Kelvin temperture to Celsius using formula: 0 K − 273,15 = -273,1 C"""
    if not tmp:
      return 0
    if float(tmp):
       celsius=tmp-273.15
       return celsius
    else:
       return 0

def kelvin_to_Farenheit(tmp:float)->float:
    """Converts Kelvin temperture to Farenheit using formula (0 K − 273,15) × 9/5 + 32 = -459,7 F"""   
    if not tmp:
      return 0
    if float(tmp):
       farenheit=(tmp-(273.15)) * 9/5 + 32
       return farenheit
    else:
        return 0

def farenheit_to_Kelvin(tmp:float)->float:
    """Converts Farenheit temperture to Kalvin using formula (0 °F − 32) × 5/9 + 273,15 = 255,372 K"""   
    if not tmp:
      return 0
    if float(tmp):
       kelvin=((tmp-32)*(5/9))+273.15
       return kelvin
    else:
       return 0




def convert_temperature(value : float = 0, from_unit: str="celsius", to_unit: str="farenheit")->float:
   """Performs the conversion between temperatures."""
   types_temp={"farenheit","celsius","kelvin"} #set for types of temperatures
   temp_converter={'CF': celsius_to_Farenheit,'CK':celsius_to_Kelvin, 'FC':farenheit_to_Celsius, 'KC':kelvin_to_Celsius,'KF': kelvin_to_Farenheit, 'FK':farenheit_to_Kelvin}
   if not value or not from_unit or not to_unit:
      return 0
   if float(value):
      if from_unit in types_temp and to_unit in types_temp:
         #Celsius to Farenheit
         if from_unit=="celsius" and to_unit=="farenheit":
            CF=temp_converter.get('CF')
            return (CF(value))
         #Celsius to Kelvin
         elif from_unit=="celsius" and to_unit=="kelvin": 
            CK=temp_converter.get('CK')
            return(CK(value))
         #Farenheit to Celsius
         elif from_unit=="farenheit" and to_unit=="celsius": 
            FC=temp_converter.get('FC')
            return (FC(value))
         #Kelvin to Celsius 
         elif from_unit=="kelvin" and to_unit=="celsius":
            KC=temp_converter.get('KC')
            print(KC(value))
            return(KC(value))
         #Kelvin to Farenheit 
         elif from_unit=="kelvin" and to_unit=="farenheit":
            KF=temp_converter.get('KF')
            print(KF(value))
            return(KF(value)) 
         #Farenheit to Kelvin
         elif from_unit=="farenheit" and to_unit=="kelvin":
            FK=temp_converter.get('FK')
            print(FK(value))
            return(FK(value))  
      else:
         return 0
   return 0
      
  
def get_input():
    while(True):
       try:
         print("Converter of temperature")
         value=int(input("Please enter temperature value: "))
         print("Please enter from unit, or to unit by using following syntax : 'farenheit','celsius','kelvin'")
         from_unit=input("Please enter from unit: ")
         to_unit=input("Please enter to unit: ")
         return value,from_unit,to_unit
       except:
          print("Please enter valid values")

def main()->None:         
    res=get_input()
    value=res[0]
    from_unit=res[1]
    to_unit=res[2]
    
    # value=37
    # from_unit="celsius"
    # to_unit="kelvin"
    # convert_temperature(37,"farenheit","kelvin")
    r=convert_temperature(value,from_unit,to_unit)
    print(f"Result: {r}")    


if __name__=="__main__":
    main()
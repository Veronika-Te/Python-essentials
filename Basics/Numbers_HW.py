#Homework numbers

import decimal
import fractions 

#Write a Python program that asks the user for two numbers and prints their sum.
def take_input_int():
  while(True):
    try:
      num1=int(input("Input first number  "))
      num2=int(input("Input second number  "))

      return num1,num2
    except ValueError:
       print("Invalid input. Please enter integer values.")


# addition, subtraction, multiplication, and division.
def add_input_nums(num1,num2):
  return num1+num2 

def substract_input_nums(num1,num2):
  return num1-num2

def divide_input_nums(num1,num2):
  if num2 ==0:
    raise ZeroDivisionError("Cannot divide by zero")
  division = num1 / num2  # Regular division
  floor_division = num1 // num2  # Floor division
  modulo = num1 % num2  # Modulo operation

  return {
    "division": division,
    "floor_division": floor_division,
    "modulo": modulo
    }


def multiply_input_nums(num1,num2):
  return num1 * num2

#casting
def cast_res_to_float(tup):
  """Casts input tuple of integers to float numbers"""
  if isinstance(tup, tuple):
    f1=float(tup[0])
    f2=float(tup[1])
    return f1,f2
  else:
    raise TypeError

def cast_res_to_complex(tup):
  """Casts input tuple of integers to complex numbers"""
  if isinstance(tup, tuple):
    c1=complex(tup[0])
    c2=complex(tup[1])
    return [c1,c2]
  else:
    raise TypeError
  
#comparing
def compare_numbers(num1, num2):
  comparisons={
    "num1 > num2": num1 > num2,
    "num1 < num2" : num1<num2,
    "num1 == num2": num1==num2,
    "num1!= num2": num1!=num2,
    "num1 >= num2": num1 >=num2,
    "num1 <= num2" : num1<=num2,
  }
  return comparisons

def compare_different_types_of_nums(num1: int, num2:int):  
  """Creates and Compares Numbers of Different Types"""
  if not isinstance(num1,int) and isinstance(num2,int):
    raise TypeError
  
  print("Compare an integer and a float")  
  print(f"Checking if the integer ({num1}) is greater than the float({num1})....?")
  if int(num1) > float(num1):
    print(f"True: {int(num1)} > {float(num1)}")
  else:
    print(f"False: {int(num1)} is not greater than {float(num1)}")

  print("Compare a decimal and a float")
  dec_num=decimal.Decimal(f"{num1}.{num2}")
  print(f"Checking if the decimal {dec_num}) is greater than the float({num1})....?")
  
  if dec_num > float(num1):
    print(f"{dec_num} > {float(num1)}")
  else:
    print(f"False: {dec_num} < {float(num1)}")

  print("Compare two fractions")
  frac1=fractions.Fraction(num1, num2)
  frac2=fractions.Fraction(num2,num1)
  print(f"Checking if the {frac1} > {frac2}")
  if frac1>frac2:
    print(f"True: {frac1} > {frac2}")
  else:
    print(f"False: {frac1} is not greater than {frac2}")  

  
def operate_integers(num1, num2):
    print("\n--------Integer numbers--------\n")
    sum=add_input_nums(num1,num2)
    print(f"num1 : {num1}, num2: {num2} ")
    print(f"Sum: {sum}")
    dif=substract_input_nums(num1, num2)
    print(f"Difference result:  = {dif}")

    div=divide_input_nums(num1, num2)
    print(f"Division result: = {div}")

    mul=multiply_input_nums(num1, num2)
    print(f"Multiplication result: = {mul}")

def operate_floats(num1, num2):
    print("\n--------Float numbers--------\n")
  
    fl_sum=add_input_nums(num1,num2)
    print(f"Sum: {num1} + {num2} = {fl_sum}")
    dif=substract_input_nums(num1,num2)
    print(f"Difference: {num1} - {num2} = {dif}")
    #division
    div=divide_input_nums(num1,num2)
    print(f"Division:{div}")
    
    mul=multiply_input_nums(num1, num2)
    print(f"Multiplication: {num1} * {num2}={mul}")

def operate_fractions(frac1, frac2):
  """Takes two fractions and perform addition, subtraction, multiplication, and division manually"""
  print("\n_______Operations with fractions_______\n")
  print(f"Fraction1: {frac1}, fraction2: {frac2}")
  
  add_res=frac1 + frac2
  print(f"Sum: {add_res}")
  sub_res=frac1-frac2
  print(f"Sub: {sub_res}")
  mul_res=frac1 * frac2
  print(f"Multiply: {mul_res}")
  div_res=frac1/frac2
  print(f"Division: {div_res}")

def operate_complex_numbers(num1, num2):
    """Creates Complex numbers and perform addition, subtraction, multiplication, and division."""
    print("\n--------Complex numbers--------\n")

    sum=add_input_nums(num1,num2)
    print(f"Sum: {num1} + {num2} = {sum}")
    dif=substract_input_nums(num1,num2)
    print(f"Difference: {num1} - {num2} = {dif}")

    #Division сomplex numbers

    mul=multiply_input_nums(num1,num2)
    print(f"Multiplication: {num1} * {num2}={mul}")


def main(): 
  try:
    res=take_input_int()
    operate_integers(res[0],res[1])
    #float
    float_tuple=cast_res_to_float(res)
    operate_floats(float_tuple[0],float_tuple[1])
    
    #complex
    complex_num_ls=cast_res_to_complex(res)
    print(f"Complex num1 : {complex_num_ls[0]}, Complex num2 : {complex_num_ls[1]}")
    operate_complex_numbers(complex_num_ls[0],complex_num_ls[1])
    
    #fractions
    frac1 = fractions.Fraction(2, 3)
    frac2 = fractions.Fraction(5, 4)
    operate_fractions(frac1, frac2)

    print("\n--------Comparing different types--------\n")
    compare_different_types_of_nums(res[0],res[1])

    test_cases=[(-5, 18), (10,5)]
    for num1, num2 in test_cases:
      print(f"\nComparing {num1} and {num2}:")
      results = compare_numbers(num1, num2)
      for expr, result in results.items():
        print(f"{expr}: {result}")

    

  except Exception as e :
    print(e)

if __name__=="__main__":
  main()
  


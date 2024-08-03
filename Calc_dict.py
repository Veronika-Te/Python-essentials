
def add(x: int, y: int)->int:
  return x + y

def sub(x: int, y: int)->int:
  return x - y

def mul(x: int, y: int)->int:
  return x * y

def div(x: int, y: int)->int:
  if y == 0:
    raise ZeroDivisionError("Hey bro you can't divide by zero")
  return x // y

calculator = {'+': add, '-': sub, '*': mul, '/': div}


def calculate(operand1, operand2, operator):
    """Uses this dictionary to perform the requested operation."""
    operations=["add","substract","multiply","division"]
    x=calculator.get(operator)(operand1, operand2)
    value=calculator.get(operator)
    
    if operator=='+':
       print("Result of", operations[0])
    elif operator=='-':
       print("Result of", operations[1])
    elif operator=='*':
       print("Result of", operations[2])
    elif operator=='/':
       print("Result of", operations[3])
    print(f"{x}")
       
def main():
    print("Calculator")
    operator = input("Enter operation: ")
    operand1 = int(input("Enter value of x: "))
    operand2 = int(input("Enter value of y: "))
    calculate(operand1, operand2, operator)
   
   

if __name__=="__main__":
    main()

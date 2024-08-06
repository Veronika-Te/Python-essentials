# # Create a lambda function that returns another 
# # lambda function which multiplies its argument by a given factor.
another=lambda x, n : lambda x, n: x *n
print("Result of lambda that return another lambda: ")
print(another(3,7)(3,7))

#Write a function make_adder(n) that returns a function that adds n to its argument.
def make_adder(n=0):
    """Returns a function that adds n to its argument."""
    def func():
        nonlocal n
        print(n+n)
    return func


#Write a function compose(f, g) 
#that returns a new function which is the composition of the functions f and g.
def f(str):
    return(str + "  " + "and I'm f ")
def g():
    return "hello I'm g"
def compose(func1,func2):
    """Returns a new function which is the composition of the functions f and g."""
    return func1(func2())

print("\n")
print("____Compose function (f,g)")
d=compose(f, g)
print(d)

# Implement a function power_factory(n) 
# that returns a function which raises its argument to the power of n.
def power_factory(n):
    def pow():
        nonlocal n
        return (n ** n)
    return pow 



# Use the map function with a lambda to square all elements in a list.
numbers=[1,2,3,4,5]
m=map(lambda x: x**2 , numbers)
print("___Result of map function: ")
for i in m:
    print(i)
print("\n")

#Use the filter function with a lambda to filter out all even numbers from a list.

numbers=[1,2,3,4,5]
f=filter(lambda x: x%2!=0, numbers)
print("____Result of filter function: ")
for i in f:
    print(i)
print("\n")

# Implement a function make_greeting(greeting) that takes a greeting string and returns 
# a function that takes a name and prints the greeting followed by the name.

def make_greeting(greeting):
    def func(name):
        return greeting + name
    return func


# Write a function make_accumulator(start=0) that returns a function which adds its 
# # argument to start and returns the new total each time it is called.
def make_accumulator(start=0):
    """Returns a function which adds its  argument to start and returns the new total each time it is called."""
    def adder(n):
        return n + start
    return adder 


# Implement a function make_config(key, value) that returns a 
# function which, when called, returns a dictionary with the given key-value pair.

def make_config(key,value):
    def make_dict():
        my_dict=dict()
        my_dict[key]=value
        return my_dict
    return make_dict



# #Write a function make_logger(level) 
# #that returns a function which logs messages with the specified log level.

def make_logger(level):
    def logs_messages():
        levels={"DEBUG", "INFO", "WARNING", "DEBUG", "CRITICAL"}
        if level.isalpha() and level in levels:
           if level=="DEBUG":
              print ("This is a debug message.")
           elif level=="INFO":
              print("This is an info message.")
           elif level=="WARNING":
              print("This is a warning message.")
           elif level=="ERROR":
              print("This is an error message.")
           elif level=="CRITICAL":
              print("This is a critical message.")
           else: 
              return "Invalid level of severity "
           return " "
        else:
           return "Invalid level of severity"
    return logs_messages

#Log
print("___Result_make_logger")
m=make_logger("DEBUG")
print(m())

#Implement a function make_memoize(f) that takes a function f and returns a 
# #memoized version of f which caches results to avoid redundant computations.
def calculate_square1(x):
    if not x:
       return
    return x**2 

def make_memoize1(func):
    cache={}
    def inner(x):
        if x not in cache:
           cache[x]=func(x)
           print(cache)
        else: 
            return cache[x]
    return inner
res=make_memoize1(calculate_square1)
print("Make memoize")
print("Checking cache")
res(2)
res(3)
res(3)
res(4)

# Write a function bar(n) that returns a list of functions. 
# Each function should be created by a nested closure and should multiply its argument by the corresponding index. Verify the closures by inspecting their __closure__ attributes.
#undone

def main():
    print("____Adder")
    f=make_adder(2)
    f()
    print("\n")


 
    print("_____Power of factory")
    p=power_factory(2)
    print(p())
    print("\n")

    
    make_greeting("Greetings!")
    f=make_greeting("Greetings!")
    print("____Result of make_greeting function: ")
    print(f("Anny"))
    print("\n")

    a=make_accumulator(7)
    print("____Result of make_accumulator function(call1):")
    print("Total: ", a(3))
    print("\n")
    
    b=make_accumulator(20)
    print("____Result of make_accumulator function(call2):")
    print("Total: ",b(2))
    print("\n")
    
    print("___Result of make_config")
    mc=make_config(1,'a')
    print(mc())
    print("\n")


if __name__=="__main__":
    main()
      

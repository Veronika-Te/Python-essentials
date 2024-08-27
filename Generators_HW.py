# 1)Fibonacci generator
# def fibonacci_sequence():
#     a = 0 
#     b = 1
#     while True:
#         c = a + b;
#         a =b; 
#         b =c
#         yield a
        
# # Accept input from the user
# n = int(input("Input the number of Fibonacci numbers you want to generate? "))

# print("Number of first ",n,"Fibonacci numbers:")
# fib = fibonacci_sequence()
# for i in range(n):
#     print(next(fib),end=" ")

#############################################
# 2)Prime generator
# def is_prime(n):
#     if n <= 1:
#        return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#            return False
#     return True

# def prime_nums_generator():
#     n = 2
#     while True:
#         if is_prime(n):
#             yield n
#         n += 1

# # Create the generator object
# primes = prime_nums_generator()

# # Accept input from the user
# n = int(input("Input the number of prime numbers you want to generate? "))

# # Generates and prints the first n(count) prime numbers
# print("First",n,"Prime numbers:")
# for _ in range(n):
#     print(next(primes))

#############################################
# #3) Infinite sequence
# def infinite_sequence():
#     start=1
#     while True:
#         start +=1
#         yield start
# #Generator
# nums_gen=infinite_sequence()

# print_count=10

# for _ in range(print_count):
#     print(next(nums_gen))

#############################################
# #4) Squares 1 to 20
# square_gen=(x**2 for x in range(1,21))
# for _ in range(1,21):
#     print(next(square_gen))

# #############################################
# #5) Read file line by line, using generator
# def read_file_lines(file_path):
#     with open(file_path) as file:
#         for line in file:
#             yield line
            
            
# file_path="Hello.txt"
# #Generator
# read_file_gen=read_file_lines(file_path)

# # for line in read_file_gen:
# #     print(line, end=" ")

###############################################
#6) Repeat(yields the given element a specified number of times.)
# def repeat_elements(element, times):
#     if isinstance(times, int):
#        for i in range(0,times):
#            yield element
        
# # ele='a'
# # t=3
# ele=3
# t=7

# repeat_gen=repeat_elements(ele,t)
# print(repeat_gen)
# for i in repeat_gen:
#     print(i, end=" ")

###############################################
#7) Mimics range function, but step is float

# def custom_range(start,end,step):
#     if not isinstance(start,int) or not isinstance(end,int) or not isinstance(step,float):
#        return
#     while(start<end):
#         yield start
#         start +=step

# start=1
# end=5
# step=0.5
# #Generator
# range_gen=custom_range(start, end, step)
# for i in range_gen:
#     print(i)

###############################################
#8)Use a generator expression to filter and yield only even numbers from a list of numbers. 
#Test this generator with a list of integers from 1 to 50.

# lst=[num for num in range(1,51)]
# #Generator expression
# even_gen = (num for num in lst if num % 2 == 0)
# print(type(even_gen))
# for i in even_gen:
#     print(i, end=" ")
    
###############################################
#9)Create two generators: gen1() yields numbers from 1 to 5, and gen2() 
#uses yield from to yield all values from gen1() and then yields numbers from 6 to 10. Print all values yielded by gen2().

# def gen1():
#     for i in range(1,6): 
#         yield i
# def gen2():
#     g1=gen1() 
#     yield from g1
#     for i in range(6,11):
#         yield i
    
# g2=gen2()
# for i in g2:
#     print(i)
     
###############################################
#10) Exception_propagator
# from typing import Iterable
# def exception_propagator(iterable):
#     if not isinstance(iterable,Iterable):
#         return "0"
#     if not iterable:
#         return "0"
#     for ele in iterable:
#         if ele=="error":
#            yield ele
#     return "There are no errors occured"
    
  
# lst=["hello","error","bye","error"]  
# #lst=["hello","bye"]
# #lst=[]
# exc_gen=exception_propagator(lst)
# #print(exc_gen)

# for ele in exc_gen:
#     print(ele)
   
###############################################
# 11) Reduce
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    yield value
tup = (2,1,0,2,2,0,0,2)
init=6
red_gen=reduce(lambda x, y: x+y, tup,init)
print("___Custom Reduce_____Generator___") 

print(red_gen)
for i in red_gen:
    print(i)

##############################################
# 12) Develop a generator function custom_zip(*iterables) that mimics the behavior of the built-in zip() function. 
# It should yield tuples containing items from each iterable passed as arguments, 
# stopping when the shortest iterable is exhausted. Test your generator with two or more lists of different lengths.

def custom_zip(*iterables, strict=False) ->list: #iterables=tuple
    """Represents zip function. Iterates over each element in the iterables, calculates the minimum length of list( in iterables). By iterating in the size of minimum length,
    creating couples of elements based on their positions in the lists(in iterables), then these couples appends to list, which casts into tuple type and returned"""
    if not iterables:
       return []
    #using built in min function
    min_length = min(len(it) for it in iterables)
    #res = [tuple([item[i] for item in iterables]) for i in range(min_length)]
    
    for i in range(min_length):
        tmp=[]
        for item in iterables:
            tmp.append(item[i])
        yield tuple(tmp)
        
#Custom Zip
print("___Custom Zip_____Generator___") 
names=["James","Bob","Ann"]
ages=[23,34,16,17]
res_gen=custom_zip(names,ages)
print(res_gen)
for i in res_gen:
    print(i)
print("\n")


##############################################
#13) Filter
def custom_filter(fn, iterable):
     if fn is None:
        for item in iterable:
            if item == True:
               yield item
     else:
        for item in iterable:
            if fn(item):
               yield item
               
lst=[1, 2, 3, 4, 5, 6]
#Generator
filter_gen=custom_filter(lambda x: x % 2 == 0  , lst)
print("___Custom Filter_____Generator___") 
print(filter_gen)
for i in filter_gen:
    print(i)
###############################################
#14)  Map
def add_2(*iterables):
    if not iterables:
        return []
    n=2
    res=[]
    for i in iterables:
        for j in i:
            res.append(j+2)
    return res     

def custom_map(operation: callable, *iterables):
    """Represents map function.Iterates over each element in the iterable 
    and applies operation to the elements, appends to list and returns"""
    if not iterables or not operation:
        return []
    for items in zip(*iterables): #iterables=([1, 2, 3], [3, 4, 7]), 1 cycle items=(1,3) 2) (2,4) 3) (3,7)
        res=operation(items)
        yield res

#Multiple adds map
print("___Custom Map_____Generator___")

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
res=custom_map(add_2, numbers1,numbers2)
print(res)

for i in res:
    print(i)
print("\n")

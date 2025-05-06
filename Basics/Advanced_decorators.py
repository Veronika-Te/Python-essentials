import time
import typing
import inspect
import functools

def execution_timer(fn: typing.Callable):
  """Measures and prints the time taken by the decorated function to execute."""
  def inner(*args, **kwargs):
    start=time.time()
    res=fn(*args, **kwargs)
    end=time.time()
    print(f"Time : {(end-start):.6f}")
    return res
  inner.__name__=fn.__name__
  inner.__doc__=fn.__doc__
  print(f"Name: {inner.__name__}")
  print(f"Docstring: {inner.__doc__}")
  inner.__signature__= inspect.signature(fn) #for help()
  print(f"Signature: {inner.__signature__}")
  return inner

######with functools
def timer_wraps(fn: typing.Callable):
  """Decorator that measures and prints the execution time of the decorated function.
    It uses functools.wraps to preserve the metadata (such as the function’s name and docstring) of the original function."""
  @functools.wraps(fn)
  def inner(*args, **kwargs):
    start=time.time()
    res=fn(*args, **kwargs)
    end=time.time()
    print(f"Time : {(end-start):.6f}")
    return res
  return inner


def log_execution(func):
  """Logs the name of the function being executed along with its arguments and return value"""
  def inner(*args, **kwargs):
    print(f"Calling function: {func.__name__}")
    print(f"Arguments: args={args}, kwargs={kwargs}")
    result=func(*args, **kwargs)
    print(f"Return value: {result}")
  return inner


def require_login(func):
  """Allows a function to execute if a global variable is_logged_in is True. If not, raise an exception."""
  def wrapper(*args, **kwargs):
    if not is_logged_in:
      raise PermissionError("User must be logged in to access this function")
    return func(*args, **kwargs)
  return wrapper

@require_login
def view_profile():
  print("Accessing user profile...")

@log_execution
def substract(a: int , b: int):
  return a - b

@execution_timer
def add(x: int, y:int):
  """Adds to integers"""
  return x+y

@timer_wraps
def say_hello(): 
  """Says hello"""
  print("Hello")

def main():
  add(3,5)
  help(add)
  substract(7,1)
  say_hello()
  help(say_hello)


  is_logged_in = True
  view_profile()


if __name__=="__main__":
  main()



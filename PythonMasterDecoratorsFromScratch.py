# W:\Perso\backup\IT stuff\Cours de programmation\Python\Udemy - Intermediate Python Master Decorators From Scratch
def greet():
    return "Hello, there!"


greet()


# --------------------------------------------------------
def greet(name):
    return f"Hello, {name}!"


greet('Julien')


# --------------------------------------------------------
def greet(name="stranger"):
    return f"Hello, {name}!"


greet()
greet('Julien')

# --------------------------------------------------------
"""
Skill Challenge: Averaging Grades define a new function called calculate_average

    it takes a single parameter called numbers, which should be a python list
    if numbers is an empty list, the function should print out a message saying 'No numbers provided and return None
    if numbers is not an empty list, the function should return the arithmetic average (i.e the mean) of the numbers also, before returning the average, the function should print out a message stating the count of numbers and the calculated average, e.g. "Count: 2 Average: 3.1"
"""
import statistics

numbers = [6, .2]


def averaging_grade(numbers):
    if not numbers:
        print(f'No numbers provided and return None')
        return None
    else:
        return (statistics.mean(numbers))


print(f'Count: {len(numbers)} Average: {averaging_grade(numbers)}')


# --------------------------------------------------------
def greet(name):
    print(f"Hello, {name}!")


def greet(name, other_name):
    print(f"Hello, {name} and {other_name}!")


greet("Andy", "Yona")


def greet(*args):
    print(f"Hello {' and '.join(args)}")


print("\n")
greet("Andy")
greet("Andy", "Yona", "John", "Doe")


# --------------------------------------------------------
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("\n")
introduce(name="Jane Bistro", age=27, country="USA")
"""
*args -> positional args
**kwargs -> keyworded args 
"""


# --------------------------------------------------------
# The technical term for a function that accepts any number of arguments is variadic function
# alternatively we can say the function signature has variable arity
def func(*args, **kwargs):
    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print(k, v)


print("\n")
func(1, 2, 3, name="Lisa Bohn", country="Germany")

# --------------------------------------------------------
"""
Skill Challenge: Variadics
modify the calculate_average function so it accepts a variable number of positional arguments, instead of a single python list.
In addition, add an optional keyword argument called "round_to", which should accept an integer and round the average to that many decimal places before returning it. 
Calculate_average[1, 2, 3, 4, 5] # Count: 5, Average: 3.0 calculate_average(1, 2.1, 3.123, 4.070001, 5, round_to=3) # Count: 5, Average: 3.059
"""


def calculate_average(*args, round_to=2):
    if not args:
        print("No numbers provided")
        return None

    total_sum = sum(args)
    count = len(args)
    average = total_sum / count
    round_average = round(average, round_to)

    print(f"Count: {count}, Average: {round_average}")
    return average


print("\n")
print(calculate_average(1, 2.1, 3.123, 4.070001, 5, round_to=3))

# --------------------------------------------------------
"""
High-Order Functions
funcs as arguments?
"""


def loud(func):
    def wrapper():
        return func().upper() + "!!!"

    return wrapper


# HOFs Higher Order Functions
# take one or more functions as their arguments, or
# return a function as its result
def greet():
    return "Hello, there"


loud_greet = loud(greet)

print(loud_greet())

# --------------------------------------------------------
"""
Skill Challenge: Arithmetic HOF

Define an HOF called 'double', that takes a function as its argument, and returns a modified version of it where the output of that func is multiplied by 2
define another function, 'add' that takes two arguments and returns their sum
apply the 'double' HOF to 'add' and store the result in a new function 'double_add', which when invokes should return the sum of two numbers multiplied by 2
add(1, 2) # Output: 3, because 1+2 = 3 double_add(1, 2) # Output: 6, because (1+2)2 = 6 double_add(5, 10) # Output: 30, because (5+10)2 = 30
"""
from operator import add


def double(func):
    def wrapper(*args):
        return func(*args) * 2

    return wrapper


double_add = double(add)

print(double_add(1, 2))
print(double_add(5, 11))

# --------------------------------------------------------
"""
First-Class Functions
"""


def loud_greeting(name):
    return f"HELLO {name.upper()}!!!"


def quiet_greeting(name):
    return f"Hello, {name}..."


def greet(name, greeting):
    return greeting(name)


greet("Andy", loud_greeting)
greet("Andy", quiet_greeting)

# let's make what we wrote above a bit clearer

from typing import Callable


def greet(name: str, greeting: Callable[[str], str]) -> str:
    return greeting(name)


# --------------------------------------------------------
"""
Closures
"""


def outer(x):
    def inner(y):
        return x + y

    return inner


closure = outer(10)
closure(6)
closure(12)


def make_multiplier(x):
    def multiplier(n):
        return x * n

    return multiplier


times_two = make_multiplier(2)
times_three = make_multiplier(3)
times_three(4)
times_two(7)

# --------------------------------------------------------
"""
Skill Chalenge: Counter Factory
Define a function called 'create_counter' that returns a 'counter' function that retains/remembers its own state, i.e. a closure.

The 'counter' function should increment the count each time it is called, before returning it.

As a bonus, implement 'create_counter' so that it takes a parameter called 'start' that determines the starting count for the counter it returns, if no start value is provided, 
'start' should default to 1
"""


def create_counter(start=0):
    count = [start]

    def counter():
        count[0] += 1
        return count[0]

    return counter


print("\n")
counter_one = create_counter(10)
res_1 = counter_one()
counter_two = create_counter(res_1)
res_2 = counter_two()
print(res_1, res_2)
counter_three = create_counter()
res_3 = counter_three()
print(res_1, res_2, res_3)

# --------------------------------------------------------
"""
Basic Introduction to Decorators
"""


def fry():
    return "Frying the food!"


def grill():
    return "Grilling the food!"


def boil():
    return "Boiling the food!"


# '@' - pie decorator syntax


def seasoning(chef):
    def wrapper():
        print("Adding some salt and pepper!")
        return chef()

    return wrapper


@seasoning
def fry():
    return "Frying the food!"


@seasoning
def grill():
    return "Grilling the food!"


def boil():
    return "Boiling the food!"


print("\n")

fry()
"""
Adding some salt and pepper!
Frying the food!
"""

grill()
"""
Adding some salt and pepper!
Grilling the food!
"""

boil()
"""
Boiling the food!
"""

print("\n")
seasoned_boil = seasoning(boil)
seasoned_boil()
"""
Adding some salt and pepper!
Boiling the food!
"""

# --------------------------------------------------------
"""
Skill Challenge - Let's Log
define a decorator called 'logger' that logs out the function name and args/kwargs of the function it is applied to as well as the result that the function returns.
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} returned: {result}')
        return result

    return wrapper


@logger
def calculate_sum(a, b):
    return a + b


print("\n")
calculate_sum(3, 6)

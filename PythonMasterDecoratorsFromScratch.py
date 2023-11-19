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


greet("Andy")
greet("Andy", "Yona", "John", "Doe")


# --------------------------------------------------------
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


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


func(1, 2, 3, name="Lisa Bohn", country="Germany")


# --------------------------------------------------------
"""
Skill Challenge: Variadics
modify the calculate_average function so it accepts a variable number of positional arguments, instead of a single python list.
In addition, add an optional keyword argument called "round_to", which should accept an integer and round the average to that many decimal places before returning it. 
Calculate_average[1, 2, 3, 4, 5] # Count: 5, Average: 3.0 calculate_average(1, 2.1, 3.123, 4.070001, 5, round_to=3) # Count: 5, Average: 3.059
"""


def calculate_average(*args, **kwargs):
    sum = 0
    Count = 0
    for i, arg in enumerate(args):
        sum += arg
        Count = i + 1
    return Count, round(sum / Count, 3)


print(calculate_average(1, 2.1, 3.123, 4.070001, 5, round_to=3))


# --------------------------------------------------------
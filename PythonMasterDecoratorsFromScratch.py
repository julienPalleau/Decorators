# # W:\Perso\backup\IT stuff\Cours de programmation\Python\Udemy - Intermediate Python Master Decorators From Scratch
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
print(times_three(4))
print(times_two(7))

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

# --------------------------------------------------------
"""
Skill Challenge - Lotto Draws

Define a decorator called 'repeat' that invockes a function of variable/unknown arity twice then, define a function called 'lotto_draw' that takes a start and end number as
arguments and returns a number that is randomly drawn from that range (inclusively) decorate 'lotto_draw' with 'repeat' to get 2 ranom numbers
"""

print("\n")


def repeat(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


from random import randint


@repeat
def lotto_draw(start_number, end_number):
    number = randint(start_number, end_number)
    print(f"Randomly drawn number: {number}")


lotto_draw(1, 49)

# --------------------------------------------------------
"""
Skill Challenge - Writing A Timer

Define a decorator called 'timed' that measures the amount of time a given function takes to run and prints that out in seconds then, define a function that takes some number of
seconds to run (e.g. a long loop) and rdecorate it with 'timed'
"""
import time


# Solution 1
def timed(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"Solution 1: Function {func.__name__} took {round(end_time - start_time, 4)} seconds to execute.")
        return result

    return wrapper


# Solution 2
def timed(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"Solution 2: Function({func.__name__}) took {round(end_time - start_time, 4)} seconds to execute.")
        return func(*args, **kwargs)

    return wrapper


@timed
def loop_this_many_times(n=10 ** 8):
    for i in range(n):
        pass


loop_this_many_times()

# --------------------------------------------------------
"""
Decorators With Arguments
"""


def ensure_healthy_workout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 500:
            print("This workout was not intense enough!")
        else:
            print(f"Well done! Target exceeded by {result - 500} calories")

    return wrapper


@ensure_healthy_workout
def calories_burned(duration_in_minutes, calories_burned_per_minute):
    return duration_in_minutes * calories_burned_per_minute


calories_burned(30, 10)


# now let's try something more flexible where we can pass as argument the calories_target
def ensure_healthy_workout(calories_target):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result < calories_target:
                print("This workout was not intense enough!")
            else:
                print(f"Well done! Target exceeded by {result - calories_target} calories")

        return wrapper

    return actual_decorator


@ensure_healthy_workout(calories_target=700)
def calories_burned(duration_in_minutes, calories_burned_per_minute):
    return duration_in_minutes * calories_burned_per_minute


print("\n")
calories_burned(30, 30)

# --------------------------------------------------------
"""
Skill Challenge - Repeated Lotto Draws
"""


def repeat(num_times):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(num_times):
                result.append(func(*args, **kwargs))
            return (sorted(result))

        return wrapper

    return actual_decorator


import random


@repeat(num_times=7)
def lotto_draw(start, end):
    return random.randint(start, end)


print("\n")
print(lotto_draw(1, 49))

# --------------------------------------------------------
"""
Chaining Multiple Decorators
"""


# available decorators

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def split(func):
    def wrapper():
        result = func()
        return result.split()

    return wrapper


"""
The way to read the the chained operator is from the closest to the function up to the farest so here: @uppercase -> @split. In addition the order of operators call, in the
example above @split @uppercase it works while
@uppercase @split won't work as split as no upper method: "Horizontal Omit Station Reflection".split().upper() => AttributeError: 'list' object has no attrivute 'upper'
"""


# target function
@split
@uppercase
def passphrase():
    return "Horizontal Omit Station Reflection"


print("\n")
print(passphrase())

# --------------------------------------------------------
"""
Preserving Identify With @wraps
"""


def split(func):
    def wrapper():
        result = func()
        return result.split()

    return wrapper


def passphrase():
    """Returns a string."""
    print("Horizontal Omit Station Reflection")


print("\n")
print(passphrase)
print(passphrase.__name__)
print(passphrase.__doc__)

"""
Now if we use a decorator we are going to loose information (name and doc)
"""


@split
def passphrase():
    """Returns a string."""
    return "Horizontal Omit Station Reflection"


print("We loose information")
print(passphrase())
print(passphrase.__name__)
print(passphrase.__doc__)

"""
In order to not loose information we use functools.
The python best practice is to always use it.
"""
from functools import wraps


def split(func):
    @wraps(func)
    def wrapper():
        result = func()
        return result.split()

    return wrapper


@split
def passphrase():
    """Returns a string."""
    return "Horizontal Omit Station Reflection"


print("with functools module we don't loose anymore information")
print(passphrase())
print(passphrase.__name__)
print(passphrase.__doc__)

"""
The bigger take away is that when we decorate functions we risk masking their identity and metadata in ways that can be confusing and problematic both for debugging and
documentations purposes, so the func tool wraps utility is a convenient way to avoid that problem and it is considered best practice to use it when defining our own decorators
in python.
"""

import uuid

print(uuid.uuid4())

# --------------------------------------------------------
"""
Skill Challenge: Delaying Downloads
Writte a placeholder function called 'download(user_id, resource)' that simulates the generation of a download link. For our purposes that could simply be a uuid() or a random
alphanumeric string then define a decorator that progressively solows down the downloads for a given user by doubling the time it takes for the download link to be generated,
e.g. the first infocation happens instantly, the second one takes 1 second, the third 2 second, the fourth 4 seconds, and so on. note that the delay should be user-specific,
but not resource specific
"""
import time

user_delay = {}


def delay_decorator(func):
    def wrapper(*args, **kwargs):
        delay = user_delay.get(kwargs.get("user_id"), 0)
        user_delay[kwargs.get("user_id")] = max(1, delay * 2)

        if delay > 0:
            print(f"Your download will start in {delay}s")

        time.sleep(delay)
        return func(*args, **kwargs)

    return wrapper


from uuid import uuid4


@delay_decorator
def download(user_id, resource):
    download_uuid = uuid4()
    download_url = f"andybek.com/{download_uuid}"

    return f"Your resource is ready at: {download_url}"


# When ran in google collab, you can run it multiple times and the sleep time get increased each time.
print("\n")
print(download(2, "python"))
print(download(2, "python"))
print(download(2, "python"))
print(download(2, "python"))
print(download(2, "python"))

# --------------------------------------------------------
"""
Skill Challenge - Authentication Workflow PartI

Mock an interface

    write a basic function that exposes a menu with 3 options:

    a. View Roster
    b. Upvote
    c. Add to Roseter
    d. Quit

...each of these options invokes their own respective functions, with the exception of 'Quit' which simply exits the menu.

    'View Roster' prints a list of names and votes, in descending order by votes. For simplicity, this information is stored locally as a python list of dicts.
    'Upvote' adds 1 vote to specified user
    'Add to Roster' allows the user to add a new name to that list

"""
# application state ###
ROSTER = [
    {"name": "Alice", "votes": 12},
    {"name": "Tyler", "votes": 9},
    {"name": "Andrew", "votes": 10}
]

################

def menu():
    while True:
        print("""
    a. View Roster
    b. Upvote
    c. Add to Roster
    d. Quit
    """)

        option = input("Enter option: ").lower()

        if option == "a":
            view_roster()
        elif option == "b":
            upvote()
        elif option == "c":
            add_to_roster()
        else:
            break


def view_roster():
    sorted_roster = sorted(ROSTER, key=lambda p: p["votes"], reverse=True)
    for p in sorted_roster:
        print(f"{p['name']}: {p['votes']}")


def upvote():
    name = input("Enter the name of the person to upvote: ").lower()

    for p in ROSTER:
        if p["name"].lower() == name:
            p["votes"] += 1
            print(f"Upvoted {p['name']}!")
            return

    print("Name was not found!")


def add_to_roster():
    name = input("Enter the name of the person to add: ")
    ROSTER.append({"name": name, "votes": 0})
    print(f"Added {name} to the roster!")


menu()

# --------------------------------------------------------
"""
Skill Challenge - Authentication Workflow PartII

@authd

write a decorator called 'authd' which could be applied to any of the functions in our interface so as to require the user to be authenticated before the function is invoked

apply that decorator to the 'Add to Roster' and 'Upvote' options in the menu

Assume the authentication would be based on a username and password, which for simplicity could be stored as global variables.
"""
# application state ###
ROSTER = [
    {"name": "Alice", "votes": 12},
    {"name": "Tyler", "votes": 9},
    {"name": "Andrew", "votes": 10}
]
USERNAME = "admin"
PASSWORD = "pwd"

AUTHD_USER = set()


################
def authd(func):
    def wrapper(*args, **kwargs):
        if USERNAME not in AUTHD_USER:
            entered_username = input("Enter username: ")
            entered_password = input("Enter password: ")

            if entered_password != PASSWORD or entered_username != USERNAME:
                print("Authentication failed!")
                return

            AUTHD_USER.add(entered_username)

        func(*args, **kwargs)

    return wrapper


def menu():
    while True:
        print("""
    a. View Roster
    b. Upvote
    c. Add to Roster
    d. Quit
    """)

        option = input("Enter option: ").lower()

        if option == "a":
            view_roster()
        elif option == "b":
            upvote()
        elif option == "c":
            add_to_roster()
        else:
            break


def view_roster():
    sorted_roster = sorted(ROSTER, key=lambda p: p["votes"], reverse=True)
    for p in sorted_roster:
        print(f"{p['name']}: {p['votes']}")


@authd
def upvote():
    name = input("Enter the name of the person to upvote: ").lower()

    for p in ROSTER:
        if p["name"].lower() == name:
            p["votes"] += 1
            print(f"Upvoted {p['name']}!")
            return

    print("Name was not found!")


@authd
def add_to_roster():
    name = input("Enter the name of the person to add: ")
    ROSTER.append({"name": name, "votes": 0})
    print(f"Added {name} to the roster!")


menu()

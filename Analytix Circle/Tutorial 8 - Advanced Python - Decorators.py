# https://www.youtube.com/watch?v=JxI79kZGh6I&list=PL3JcF91tUKYYIbjAAZ2Y8UNp2IhqEAFSW&index=5
'''
Decorators look like this they have the @ sign and some sort of name: @my_decorator
but in order for us to fully understand what decorators are, we have to talk about functions in python.
And why they are so powerful, this is a neat thing about python
In python functions are what we call first-class citizens.
In python, functions are what we call first-class citizens that is they can be passed around like variables,
they can be an argument inside of a function they act just like variables.
Let me show you if I create a hello function which frankly is completely useless because all it does is say hello
if I do this:
'''


def hello():
    print('helllloooooooo')


'''
remember functions are pretty much just variables in python again something that is not always the case with all programming
languages. So if I wanted to I can say greet equals to hello so that if I print greet and I runt this I get helllloooooooo 
'''
hello()

'''
what if i just pass hello like this if i run this well i get the function location in memory so I would have to use greet
like this and run it right we have to call the hello function, what if we this what if I say delete hello a keyword in python
that deletes that function what do you think will happen? Let's see if I run this, is that what you expected?  
Did you expect greet to still work? The interesting thing about python is that I create hello and this is now created in memory
when we get to line four I say greet is going to point to hello so hello can still be called down here I can still 
say hello because hello is the name of the function that points to that location in memory but when I do delete hello
all it does is say I'm going to delete this function this name reference to this function that's in memory
however because greet a whole nother variable is still pointing to this function I'm going to delete the hello
word so if I go hello like this I'm going to get an error name hello is not defined however the greet is still pointing in memory to this location
so python is smart enough to say hey you told me to delete hello I'll delete the name hello but I'm not going to delete the function because greet
is still pointing to it. 
'''
greet = hello
del hello
print(greet)

'''
So functions in python act just like variables do the're first class citizens we can also pass functions
around inside of arguments. If I say hello and then this hello receives another function that calls let's say 
function like this well I can create a greet function let's say define greet and this function is just going to print
'still here' now in here if I call hello with greet or just we're clear let's just say a equals to hello(greet)
if I print a what will happen? That still works because what happens is I say hey call the function hello okay I'm
calling the function hello with the argument greet so we go to hello function and we say hey run function and
what's function we want to call this function because we have these brackets func() so we jump to what function is
which in our case is greet so we go over here and say hey just print this we didn't have to call it in here
because the hello function calls it for us. So why did I just teach you all of that what does that have to do with decorators?
decorators are only possible because of these features this ability of functions to act like variables act like 
fist-class citizens in python and when we start learning about decorators underneath the hood they're using this power of functions.
'''


def hello(func):
    func()


def greet():
    print('still here!')


a = hello(greet)
print(a)

'''
How to create our own decorator what they mean and expand on this idea of a decorator but
here's a short form of what decorators do:
            decorators supercharge our function 
if we had our let's say hello function here by adding some sort of a decorator like this we can supercharge our function
and add extra functionality to it, it lets the python interpreter know I want this hello function to have some extra features.
We have to understand this idea of a higher order function that is a higher order function. A higher order function can be one
of two things it could either be a function let's say the greet function that accepts another function so this right here is 
a higher order function it's a function that accepts inside of its parameters another function another way it can be a higher order
function is if it's a function that returns another function if we define let's say greet two that just runs normally but instead returns
another function so let's say in here we have define func and this define func let's say just returns five and we return the function
this is a higher order function. 
        A higher order function is any function that either  accepts a function as a parameter or returns a function
and if you're thinking hey is that map function is that a higher order function because it accepts a function yep that's a high order function
so is reduce or filter these are all higher order functions
'''


# High Order Function HOC
def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func


'''
8'40'' Let's write our own Decorators 
remember a decorator superchares our function it's simply a function that wraps another function and enhances it or changes it
but the best way for me explain what it is to actually code our own so let's do that let's define a my_decorator and 
this decorator is going to accept a function right away we should know that this is a higher order function now in here (def my_decorator())
we're going to call the function but before we do that we're actually going to wrap this function in another function so we're going to say
define the wrap function so this is just a wrapper and this wrap function is going to be a function that simply runs this func and then finally
we'll just return wrap function and notice here that I'm not calling it I'm just returning it so that later on somebody can use it.
'''


# Decorator
def my_decorator(func):
    def wrap_func():
        func()

    return wrap_func


'''
Let's say we have a simple function hello and this simple function just prints hello.
Now why is this useful? Because now I can use my_decorator(func) as decorator
python as soon as we write an a in front of this going to say hey this is going
to be a decorator and the decorator as long as we follow this syntax of accepting a function
having a wrapper function calling the function and returning the wrapper function can be used
'''
print()


# Decorator
def hello():
    print('hellloooo')


def my_decorator2(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')

    return wrap_func


'''
So if I do my_decorator see how it's all blue now this decorator can actually be used on top
when defining our functions so if we want to use my decorator on the hello function
we use it like this so that when I call hello next in my program I click run I get hello.
What we just did with the decorator hasn't change anything it works exactly as expected
but what it allows us to do is that now we can add extra functionality remember how I said that
decorators is a function like my_decorator that wraps that is here (wrap_func()) another function wich is the function
that we pass it and enhances it so how can we enhance hello, well we can do anything inside of this wrapped function
for example I can say print and then we'll just print some stars in here and maybe print another set of stars in here
so that when I call run boom we've just super boosted our hello function.
And this is why decorators are useful by just adding this one line @my_decorator2 I'm able to super boost so that 
let's say I create another function called bye and this bye is going to print see ya later by calling bye here and clicking run
well nothing changes but I wanted to super boost it just like the hello all I need to do is just copy the decorator and use it here as well
so that if I run it there we go we've super boosted our buy this is the power of decorators by
using this syntax I can add extra functionality to other functions.
'''
print()


@my_decorator2
def hello():
    print('hellloooo^_^')


@my_decorator2
def bye():
    print('see ya later')


hello()
bye()

'''
Underneath the hood all it does, well let me show you, based on what we've learned so far about
functions because they are first class citizens right all we're doing is literally this:
    we're saying variable a equals hello and wrapping this hello and calling it with my_decorator
so I'm saying my_decorator hello and then after that I am running a like this so let's say this was hello2
well I'm just running it like so, so that if I run this everything still works 
all I'm doing is wrapping my hello function with my decorator and assigning it to a variable 
so if we go step by step we see that my_decorator receives a function in our case the hello function
it then returns this wrapped function that has hello in here so we return this wrap function so hello2
now equals this wrapped function and then this wrapped function gets called and what does it get called
with well it prints this (print('**********')) then it runs the hello function and then it print this 
(print('**********')) it's the same as doing something like this we simply call it again if i run this
it works, we're calling the first function (my_decorator(func)) and the first function returns another function
and then we call the next returned function which is wrap function now the reason decorators are useful is because
instead of doing this and frankly looking confusing I can just add the @my_decorator and we don't need to do all of this
our hello gets atuomatically wrapped by my_decorator but essentially this is what the @ sign is doing.

'''
print()
hello2 = my_decorator(hello)
hello2()

'''
How to pass argument?
The one way is to just simply say: 
def my_decorator2(func):
    def wrap_func(x):
        print('**********')
        func(x)
        print('**********')

    return wrap_func
    
This wrapper function receives the parameter so let's say hi if I click run this works 
We're calling hello function with hi string as argument. So this function hello gets
passed we then receive as argument the x, remember underneath the hood my decorator
is saying a equals my decorator and hello: a=my_decorator(hello) so all we're doing is running my_decorator hello
which now turns into the wrapped function and what we do the wrapped function a
we give it an argument of hi so the wrapped function accepts this parameter
and then runs the function hello
'''
# Decorator
print()


def my_decorator3(func):
    def wrap_func(x):
        print('---------')
        func(x)
        print('----------')

    return wrap_func


@my_decorator3
def hello(greeting):
    print(greeting)


hello('hiiii')

'''
but here's the question what if greeting also had an emoji that it accepts so we're printing greeting and then the
emoji. What do we do well again we'd have to create another parameter and then another parameter and then here
a('hiiii', ;-)) call it with let's say a smiley face. If I click run this works.
'''
# Decorator
print()


def my_decorator4(func):
    def wrap_func(x, y):
        print('++++++++++')
        func(x, y)
        print('++++++++++')

    return wrap_func


@my_decorator4
def hello(greeting, emoji):
    print(greeting, emoji)


a = my_decorator4(hello)
a('hiiii', ':)')

'''
19'57''
But this is hectic every time I need to change parameters well I have to modify this and what if we had keyword arguments like
default hi:
@my_decorator4
def hello(greeting='hi', emoji):
    print(greeting, emoji)
    
There is actually a pattern here that we can use that makes things really simple for us and all we do is this
we do the star args (*args) wich we have seen wich takes all positional arguments and then star star keyword args (**kwargs)
which takes all the keyword arguments and we call the function by saying star args (*args) to unpack all the positional
arguments and star star key word args (**kwargs) to unpack all the keyword arguments.
Now check this out I can do emoji equals to let's say sadface as the keyword argument and now if I just pass
hi like this and hit run and let's just remove this as well since we don't need it we'll call hello properly because
we have the decorator and click run look at that I get high with the sad face now the reason this is called a decorator
it's because it's a famous pattern in programming it's called the decorator pattern and this:
def my_decorator5(func):
    def wrap_func(*args, **kwargs):
        print('//////////')
        func(*args, **kwargs)
        print('//////////')
    return wrap_func
is the decorator pattern it gives our decorator flexibility so that we're able to pass as many arguments as we want into our
wrapped function by using args and kwargs and then unpacking them like this: *args, **kwargs inside of a function
and this syntax let's say if we didn't even have the print statements:
 def my_decorator5(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func
is why decorator are so powerful by just using these lines of code we're able to add functionality using the decorator
pattern to decorate our functions and the decorator patterns are used all over programming so it's a very
powerful concept 
'''
print()


def my_decorator5(func):
    def wrap_func(*args, **kwargs):
        print('//////////')
        func(*args, **kwargs)
        print('//////////')

    return wrap_func


@my_decorator5
def hello(greeting, emoji=':('):
    print(greeting, emoji)


hello('hiiii')

'''
To finish of the lesson on decorator I want to talk to you about some of the ways that decorators can be useful and
some of the common locations that we're going to see decorator patterns in our code and we are going to build our own performance
decorator that's going able to tell us how our functions perform how fast they are.

So let's talk about some of the practical applications of decorators I mean we've already seen them in 
classes right we saw how class method and static method we're able to create class methods and static methods
on the class that the direct class can use and if you don't remember these just go back to those videos.
But I want to show you one of my favorite examples of a decorator we're going to create our own what we're
going to do is I want to have a performance decorator and by the way this decorator doesn't exist in python we're going
to build it from scratch what I want to do is be able to have a performance decorator that I can use
during testing my code to see how fast my code runs for example if I had a function let's say a long time that
takes a long time to complete so I'm going to do a really long loop and say for i in range of let's say all these numbers
and i'm just going to do a random calculation i times 5. This function I want to know how well it performs how many
milliseconds it takes to complete this so how can we build that so first I'm ging to do something that we haven't talked
about yet that we will something about modules in built-in modules so for now we're not going to talk about this too
much but we're going to import the time module something called well time again something that we'll talk about in
the module section of the course I'm essentially saying hey when I installed python or in my case when I'm using this
pycharm it has access to this time if I ask for it and in this case I'm saying hey I want to use this time object
or module that I get from python and in here we are going to create our decorator following the pattern we've learned
I'm going to say define performance and performance is going to accept a function just like we've seen before
and in here we'll have our wrapper so let's say wrapper function and wrapper function if you remember it's going
to be flexible by taking in *args and **kwargs so that we can pass it however many parameters we want because we 
don't know how this function how many parameters it's going to have and I want to be able to use performance
on all my functions now in here first what we're going to do is we're going to have the result of the
function be the function that we receive right here and then simply say run the function with *args and **kwargs
and finally at the end of this I want to return the results and then finally we're going to return the wrapper
so nothing we haven't seen before I could have just done return here or just ran the function but 
I'll show you why I dit it this way in a second right now our function doesn't really do anything if I click run
well nothing happens if I do long_time() and I run this function it just took a long time to run but that's 
it nothing happens this is when we make things interesting we want to caluclate from
the beginning of running this function to the end of running this function and we can use time module to do this
I can create a variable time 1 for the start and simply say time so I'm running this time function
that's going to start a time and say hey this initial time is going to be t1 and after this function our main
function long_time() gets run I'm going to say t2 and say hey what's the time right now. 
However much difference there is between  t2 and t1 is how long this part: (result = fn(*args, **kwargs)) took
so all we do is say print an f string and say it took t2 minus t1 and this actually returns a millisecond
and that's it I've wrapped my function with just this extra timepiece and then I'm printing as soon as we run the
function how long it took so let's check it out if I now run my long time function right here and I click run
all right it took 0.06 s to run.
'''
# Decorator
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5

long_time()

'''
I now have this decorator (above) that I can give pretty much any function in my program
and actually measure the performance of my function pretty useful right I could have this piece of code
and before let's say I deploy my code or put my code out into the world. I can test how performant
my functions are and maybe I can optimize things in different ways very very useful and I did that in just
a few lines of codes now mind you this peformance decorator depends on the machine and how fast your 
cpu and memory are on your computer so for what took me 19 seconds might take you a lot more or a lot less depending
on your machine but this is a nice way to compare functions relatively.
'''
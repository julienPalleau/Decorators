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


hello('hoooo', ':)')

'''
19'57''
But this is hectic every time I need to change parameters well I have to modify this and what if we had keyword arguments like
default hi:
@my_decorator4
def hello(greeting='hi', emoji):
    print(greeting, emoji)
    
There is actually a patter here that we can use that makes things really simple for us and all we do is this we
'''
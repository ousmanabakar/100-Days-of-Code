import time


def delay_decorator(function):
    def wrapper_func():
        time.sleep(5)
        # Do something before the func run
        function()
        # Do something after the func run

    return wrapper_func


# First way how to use decorators by writing "@delay_decorator" to the  func that we want to call
@delay_decorator
def say_hello():
    print("hello")


say_hello()


def say_bye():
    print("bye")


def greeting():
    print("How are you?")


# second way how to use decorators by creating new func and call it
new_decorated_func = delay_decorator(greeting)
new_decorated_func()

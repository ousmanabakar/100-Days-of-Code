class User:
    def __init__(self, name):
        self.name = name
        self.is_logged = False


def is_authenticated_deco(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged == True:
            func(args[0])
    return wrapper


@is_authenticated_deco
def create_bolg_post(user):
    print(f"This is a {user.name}'s new blog post")


new_user = User("Ousman")
new_user.is_logged = True
create_bolg_post(new_user)

"******************************************"
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You called {func.__name__}{args}")
        result = func(args[0], args[1], args[2])
        print(f"returned result {result}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)



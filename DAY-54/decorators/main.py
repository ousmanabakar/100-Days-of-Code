# def ad(x, y):
#     return x + y
#
#
# # def subtract(x, y):
# #     return x - y
# #
# #
# # def multiply(x, y):
# #     return x + y
# #
# #
# # def divide(x, y):
# #     return x + y
#
#
# def calculate(calc_func, x, y):
#     return calc_func(x, y)
#
#
# result1 = calculate(ad, 2, 5)
# # result2 = calculate(divide, 20, 5)
# # result3 = calculate(subtract, 15, 5)
# # result4 = calculate(divide, 9, 3)
# print(result1)


# def outer_func():
#     print("outer func called")
#
#     def inner_func():
#         print("inner func called")
#
#     inner_func()
#
#
# outer_func()


def outer_func():
    print("outer func called")

    def inner_func():
        print("inner func called")

    return inner_func


nested_func = outer_func()  # nested_func = inner_func
nested_func()

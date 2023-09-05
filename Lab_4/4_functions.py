# 1 example
# def sum_multi_arg(*args):
#     return sum(args)
#
# print(sum_multi_arg(2, 3, 4, -1, 23, 2.3, 2.1))
#
# #2 example, not working
# def sum_multi_arg_with_defaults(*args):
#     return sum(args)
# args = {3, 4, -1, 23, 2.3, 2.1}
# print(sum_multi_arg_with_defaults(args))

# def arb_keyword(**inp_params):
#     for ind, val in inp_params.items():
#        inp_params[ind] = val + 3
#     return inp_params
#
# print(arb_keyword(a=4, b=6))

# # 3 recursion
# def rec_call(a):
#     if a < 10:
#         print(f'the step value of a is {a}, passing to the next step value {a + 1}')
#         return a + rec_call(a + 1)
#     # without else it will try to add None to the results and fails with each call
#     else:
#         return 10
#
# print(rec_call(9))

# # 4 scope
# x = 5
# def scope_func():
#     x = 10
#     print(x)
# scope_func()
# print(x)
# # resul 10
# #       5
# def scope_func_glob():
#     global x_glob
#     x_glob = 10
# # error not defined:
# # print(x_glob)
# scope_func_glob()
# print(x_glob)

# # 5 lambda
# def lam_multiplication(a):
#     return lambda x: (x+1) * a
#
#
# double_multi = lam_multiplication(2)
# triple_multi = lam_multiplication(3)
#
# print(double_multi(1))
# print(triple_multi(1))

# 6 Decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


# @my_decorator
def say_whee():
    print("Whee!")


test = my_decorator(say_whee)
test()

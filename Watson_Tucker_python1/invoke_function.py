import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. 
When you need to perform an action more than once, wrap that code in a function and call it when you need it. 
When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print("Invoking function with a mix of default args")
introduction_with_mix_of_default_args('Tucker', 'Watson')

print("Invoking function with product of two args")
print(product_of_two_num(3, 7))

print("Invoking function add all nums")
print(add_all_nums(1, 4, 7))

print("Invoking function that doubles num")
print(double(4))

print("Invoking function that returns fib sequence")
print(fib(9))

print("Invoking function that subtracts")
print(subtract(9, 5))

print("Invoking function that returns if a string is a palindrome or not")
print(palimdrome("RACEcar"))
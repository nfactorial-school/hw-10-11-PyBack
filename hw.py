"""
Exercise-1: First-class Function Operation
Write a function "operation(func, x: int, y: int) -> int" that takes in a function 'func' and two integers, 'x' and 'y'. Apply the function to the two numbers and return the result. 

Example:
def multiply(a, b):
    return a * b
operation(multiply, 5, 3) -> 15
"""

def operation(func, x: int, y: int) -> int:
    pass

"""
Exercise-2: Implement Map Function
Write a function "my_map(func, my_list: list) -> list" that mimics the built-in Python 'map' function. It should take a function and a list as input, applying the function to each element of the list.

Example:
my_map(lambda x: x**2, [1, 2, 3, 4]) -> [1, 4, 9, 16]
"""

def my_map(func, my_list: list) -> list:
    pass

"""
Exercise-3: Lambda Function with Filter
Write a function "filter_even_numbers(numbers: list) -> list" that uses 'filter' and a lambda function to filter out all even numbers from the list.

Example:
filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]) -> [1, 3, 5, 7]
"""

def filter_even_numbers(numbers: list) -> list:
    pass

"""
Exercise-4: Recursive Factorial
Write a function "recursive_factorial(n: int) -> int" that calculates the factorial of a number recursively.

Example:
recursive_factorial(5) -> 120
"""

def recursive_factorial(n: int) -> int:
    pass

"""
Exercise-5: Decorator for Timing
Write a decorator function "timeit_decorator(func)" that prints the time taken by the function to execute.

Example:
@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]
"""

def timeit_decorator(func):
    pass

"""
Exercise-6: Function Composition
Write a function "compose(*funcs)" that takes a series of functions and returns a new function that composes them. The returned function should take an input and apply each function to the result of the previous function.

Example:
def double(x):
    return 2 * x
def square(x):
    return x ** 2
new_func = compose(double, square)
new_func(3) -> 36
"""

def compose(*funcs):
    pass

"""
Exercise-7: Partial Application
Write a function "partial(func, *args)" that implements partial application. The function should return a new function that when called will return the result of applying the input function to the provided arguments, followed by the new arguments.

Example:
def add_three_numbers(a, b, c):
    return a + b + c
add_five_and_six = partial(add_three_numbers, 5, 6)
add_five_and_six(7) -> 18
"""

def partial(func, *args):
    pass

"""
Exercise-8: Reduce to Compute Factorial
Write a function "factorial_reduce(n: int) -> int" that uses `reduce` to compute the factorial of an integer.

Example:
factorial_reduce(5) -> 120
"""

def factorial_reduce(n: int) -> int:
    pass

"""
Exercise-9: Function Memoization
Write a function "memoize(func)" that takes a function and returns a memoized version of the function. The memoized version should cache the results of the function so that the next time it's called with the same arguments, it returns the cached value instead of calculating the result again.

Example:
def expensive_function(x):
    return x ** x  # expensive calculation
memoized_function = memoize(expensive_function)
memoized_function(5)  # -> This will take some time to compute
memoized_function(5)  # -> This will return the cached result
"""

def memoize(func):
    pass

"""
Exercise-10: Custom Reduce Function
Implement your own version of Python's 'reduce' function "my_reduce(func, iterable, initializer=None)".

Example:
my_reduce(lambda x, y: x*y, [1, 2, 3, 4]) -> 24
"""

def my_reduce(func, iterable, initializer=None):
    pass

"""
Exercise-11: Lambda Function Sort
Write a function "sort_by_last_letter(words: list) -> list" that sorts a list of words in ascending order based on the last letter of each word. Use a lambda function.

Example:
sort_by_last_letter(['apple', 'banana', 'cherry', 'date']) -> ['banana', 'apple', 'date', 'cherry']
"""

def sort_by_last_letter(words: list) -> list:
    pass

"""
Exercise-12: Recursive List Reversal
Write a function "recursive_reverse(my_list: list) -> list" that reverses a list using recursion.

Example:
recursive_reverse([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def recursive_reverse(my_list: list) -> list:
    pass

"""
Exercise-13: Decorator for Function Counting
Write a decorator function "count_calls(func)" that counts the number of times a function is called.

Example:
@count_calls
def test_function():
    return

test_function()
test_function()
# Output: 'test_function' was called 2 times.
"""

def count_calls(func):
    pass

"""
Exercise-14: Use reduce to Find the Maximum Number
Write a function "find_max(numbers: list) -> int" that uses reduce to find the maximum number in a list.

Example:
find_max([1, 2, 3, 4, 5]) -> 5
"""

def find_max(numbers: list) -> int:
    pass

"""
Exercise-15: Use filter and lambda to Remove Elements
Write a function "remove_elements(my_list: list, element) -> list" that uses filter and a lambda function to remove all instances of a specific element from a list.

Example:
remove_elements([1, 2, 3, 2, 4, 2, 5], 2) -> [1, 3, 4, 5]
"""

def remove_elements(my_list: list, element):
    pass

"""
Exercise-16: Higher-Order Function for Repeats
Write a function "repeat(n: int)" that returns a function. The returned function should take a string input and repeat it `n` times.

Example:
repeat_three_times = repeat(3)
repeat_three_times('hello') -> 'hellohellohello'
"""

def repeat(n: int):
    pass

"""
Exercise-17: Recursive List Sum
Write a function "recursive_sum(my_list: list) -> int" that recursively computes the sum of a list of integers.

Example:
recursive_sum([1, 2, 3, 4, 5]) -> 15
"""

def recursive_sum(my_list: list) -> int:
    pass

"""
Exercise-18: Map with Multiple Lists
Write a function "add_two_lists(list1: list, list2: list) -> list" that uses `map` and `lambda` to add together corresponding elements of two lists.

Example:
add_two_lists([1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
"""

def add_two_lists(list1: list, list2: list) -> list:
    pass
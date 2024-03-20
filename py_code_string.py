code = '"hello" + "world"'
result = eval(code)
print(result)  # Output: "hello world"
 
code = '["a", "b", "c"][1]'
result = eval(code)
print(result)  # Output: "b"



import types
 
code_string = "a = 6+5"
my_namespace = types.SimpleNamespace()
exec(code_string, my_namespace.__dict__)
print(my_namespace.a)  # 11


code = """
numbers = [2, 3, 7, 4, 8]

def is_even(number):
    return number % 2 == 0

even_numbers = [number for number in numbers if is_even(number)]

squares = [number**2 for number in even_numbers]

result = sum(squares)

print("Original data:", numbers)
print("Even numbers:", even_numbers)
print("Square values:", squares)
print("Sum of squares:", result)
"""

exec(code)
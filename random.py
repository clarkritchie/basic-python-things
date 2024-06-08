def iterate_list(input_list):
    for item in input_list:
        print(item)

def example_function_1(**kwargs):
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")

def example_function_2(*args):
    for arg in args:
        print(arg)

# Example usage
my_list = [1, 2, 3, 4, 5]
iterate_list(my_list)

example_function_1(name="Alice", age=30, city="New York")
example_function_2(1, 2, "hello", True)
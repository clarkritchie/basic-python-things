#
# List
#
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
my_list.append(99)
print("List after appending:", my_list)

#
# Tuple
#
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
# tuples are immutable!
my_tuple += (99,)  # Note the comma to create a tuple with a single element
print("Tuple after appending:", my_tuple)

#
# Dict
#
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)

my_dict["foo"] = "bar"
print("Dictionary after appending:", my_dict)

#
# Set
#
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Create an empty set
# my_set = set()

# Append a single element to the set
my_set.add(99)
print("Set after adding one element:", my_set)

# Append multiple elements to the set using update() method
my_set.update([60, 70, 80])
print("Set after adding multiple elements:", my_set)
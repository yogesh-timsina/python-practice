'''SetExp={1,2,3,"yogesh","timsina"}
print(SetExp)
my_list=[1,2,3,4]
my_set=set(my_list)
print(my_set)
my_string="yogesh"
my_set=set(my_string)
print(my_set)'''
'''my_tuple = (1, 2, 3, 3, 4)

# Convert to set
my_set = set(my_tuple)

print(my_set)  # Output: {1, 2, 3, 4}
num=[1,2,3,3,4,2,1,6,4]
unique_num=list(set(num))
print(unique_num)
my_set = {1, 2, 3,4}
my_set.add(5)  # Adds 4 to the set
print(my_set)  # Output: {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}
my_set={1,2,3,4}
my_set.update([5,6,7])
print(my_set)
my_set = {1, 2, 3}
my_set.remove(2)  # Removes 2
print(my_set)  # Output: {1, 3}

my_set = {1, 2, 3}
my_set.discard(3)  # Removes 3
my_set.discard(5)  # No error, 5does not exist
print(my_set)  # Output: {1, 2}

# Create a set
my_set = {1, 2, 3, 4, 5}

# Display the original set
print("Original Set:", my_set)

# Using pop() to remove and return an arbitrary element
popped_element = my_set.pop()
print("Popped Element:", popped_element)
print("Set After pop():", my_set)

# Using clear() to remove all elements from the set
my_set.clear()
print("Set After clear():", my_set)
'''
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print("Set after discarding 3:", my_set)
my_set.discard(10)
print("Set after attempting to discard 10:", my_set)

colors = ["red", "blue", "green", "yellow", "brown", "black"]

# Test for membership in list
print("yellow in colors: ", ("yellow" in colors))
print("pink in colors: ", ("pink" in colors))

# Concatenate iterable of strings using ", " as delimiter
sep = ", "
print("colors: ", sep.join(colors))  

del colors[4]  # remove brown

print("removed 'brown':", "/".join(colors))

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(f"{list_c = }")

my_list = ['a', 5, 9.6]
a, b, c = my_list
print(type(a))
print(type(b))

x: float = "abc"

print(x, type(x))



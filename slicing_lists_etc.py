fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

print(fruits[0], fruits[11], fruits[-1])
print()
#    start-at:stop-before
print(fruits[0:3])
print(fruits[3:7])
print(fruits[:3])
print(fruits[15:])
print(fruits[-5:])  # start-at -5, go to end
print(fruits[-5:-1])
print(fruits[1:])
print(fruits[1:-1])  # all but first and last

x = "mango"
print(x[:3])
print(x[2:4])
print(x[-2:])

file_path = "lettuce.txt"
file_path_no_extension = file_path[:-4]
print(file_path_no_extension)
extension = file_path[-4:]
print(extension)
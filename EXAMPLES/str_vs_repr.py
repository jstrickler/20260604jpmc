from datetime import date


today = date.today()

print(today)   # uses str(today)
print(str(today))   # uses str(today)
print()
print(repr(today))  # uses repr(today)
print()
print(f"{today = }")  # also uses repr(today)
print(f"{today = !s}")  # also uses repr(today)
print(type(today))
print(today.year)

x = "abc"
print(x)
print(repr(x))

x = open('../DATA/mary.txt')
print(repr(x))
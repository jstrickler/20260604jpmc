colors = []   # empty list
fruits = list() # empty list

cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')  # insert at beginning
cities.insert(5, "Buffalo") # add as 6th element
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)  # for city in more_cities: cities.append(city)
print(f"cities: {cities}\n")

# LIST.append(obj) LIST.insert(idx, obj) LIST.extend(iterable)

del cities[3] 
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()  # remove and return last element
# city = cities[len(cities) - 1]
# del cities[len(cities) - 1]
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

# del LIST[idx]  LIST.remove(value) LIST.pop() LIST.pop(idx)    
print()
for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city.upper())

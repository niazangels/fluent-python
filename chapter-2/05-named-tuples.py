from collections import namedtuple

Person = namedtuple('Team_1', ('name', 'age', 'sex', 'location'))

alice = Person('Alice', '22', 'f', 'LAX')
bob = Person('Bob', '24', 'm', 'QNS')

Person = namedtuple('Team_2', ('name', 'age', 'sex', 'location'))

chloe = Person('Chloe', '22', 'f', 'DLW')
john = Person('John', '26', 'm', 'AUX')

print(alice)
print(chloe)

print("\nDetails available from John: {}".format(john._fields))

# Make
print("\n> namedtuple._make and nested namedtuples")
City = namedtuple('City', 'name country population coordinates')
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print("\nDelhi: ", delhi)
delhi_dict = delhi._asdict()
print("\nDelhi (dict):", delhi_dict)

print("\nThe population of Delhi is", delhi_dict['population'])
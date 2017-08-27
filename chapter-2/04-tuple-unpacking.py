import os

print("> `Simple example\n")
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))


print("\n> os.path.split() is so cool!\n")

file, folder = os.path.split('/home/karen/projects/art/skillshare.png')
print ("{} --> {}".format(file, folder))

tail, head = os.path.split('/home/karen/projects/art')
print ("{} --> {}".format(tail, head))

print("\n> Grabbing excess\n")
first, second, *rest = range(5)
print("first: {} second: {} rest: {}".format(first, second, rest))

*head, tail = range(5)
print("head: {} tail: {}".format(head, tail))

print("\n> Nested tuple unpacking\n")
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# Find out more about the format() method here: https://pyformat.info/

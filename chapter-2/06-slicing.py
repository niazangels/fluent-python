invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                 $17.50    3    $52.50
1489  6mm Tactile Switch x20            $4.95     2    $9.90
1510  Panavise Jr. - PV-201             $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240            $34.95    1    $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

print("> Assigning to slices")
l = list(range(10))
print("l =", l)
l[2:5] = [1, 2]
print("l =", l)
l[1::2] = [-1, -2, -3, -4]
print("l =", l)  # Notice how this is comes out
try:
    l[2:3] = 100
except:
    print("! Failed to assign non iterable to list")
    l[2:3] = [100]
print("l =", l)  # Notice how this is comes out

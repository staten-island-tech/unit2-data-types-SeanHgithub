""" x = 3
y = float(3)
print(x,y) """
""" values = [1,2.23,5,7,2,30,15] """
""" print(values)
for i in values:
    print(i) """
""" print(values[0])
print(values[6]) """
""" print(values[7]) """
""" x = "this is a thing"
y = x.split( )
z = y[0]
print(y)
print(z) """
""" day_of_week = input("what day is it?")
if day_of_week == "Monday":
    print("correct")
else:
    print("incorrect") """
""" x = "test"
print(f"hello {x}") """
""" temp = 75
if temp > 68:
    print("warm")
elif temp == 68:
    print("perfect")
else:
    print("cold") """
""" values = [1,2,3,4,5,6,7,8,9,10]
def odd_even(x):
    if x % 2 == 0:
        return("even")
    else:
        return ("odd")
print(values)
for i in values:
    print(i, odd_even(i)) """
""" bill_value = input("How was the service?")
if bill_value == "bad":
    print("tip 0%")
elif bill_value == "okay":
    print("tip 15%")
elif bill_value == "good":
    print("tip 20%")
elif bill_value == "great":
    print("tip 25%") """
""" def factors(x):
    for y in range(1, x +1):
        if x % y == 0:
            print(f"{y} is a factor of {x}")
factors(7) """
values = []
def gcf(x,y):
    for a in range(1, x+1):
        if x % a == 0:
            values.append(a)
    for b in range(1, y+1):
        if y % b == 0:
            values.append(b)
gcf(200,500)
values.remove(200)
values.remove(500)
print(values)


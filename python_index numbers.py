list = [1,2,3,4,5,6]
a = int(input("Please enter a number: "))
b = int(input("Please enter a second number: "))
result = []
if a < len(list) and b < len(list):
    result.append(list[a])
    result.append(list[b])
    print(result)
if a >= len(list):
    print("{} is out of range".format(a))
if b >= len(list):
    print("{} is out of range".format(b))
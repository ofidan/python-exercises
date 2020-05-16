x = [([1, 2], [3, 4, 5], (6, 7))]
y = []
for i in x:
    for j in i:
        y += j
print(y)
w = {}
for z in y:
    w[z] = str(z ** 2)
print (w)



    
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

num = [1,8,6,2,5,4,8,3,7]
cont = []
for i in range(len(num)):
    for j in range(len(num)):
        d = min(num[i], num[j]) * (j - i)
        cont.append(d)
print(max(cont))
        
# Input → x = [([1], [2, 3], (4, 5, 6))]
# Desired out → {1, 2, 3, 4, 5, 6}

# x = [([1], [2, 3], (4, 5, 6))]
# In simple word Mutable objects are not hashable.
# Example : List ,Carray , sets ,Dictionary ,Collections.deque etc.
# In any language it is considered wise to call mutable object not hashable because it's hash can be changed by it's mutability.
# Example of hashable objects: integer ,float ,tupple ,frozen sets ,string etc

x = [([1, 2], [3, 4, 5], (6, 7))]
y = []
for i in x:
    for j in i:
        y += j
print(y)

# y=[]
# x = [([1, 2], [3, 4, 5], (6, 7))]
# for i in x:
#     for j in i:
#         for k in j:
#             y.append(k)
# print(y)       


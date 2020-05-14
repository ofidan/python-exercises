num = [1, 2, 3]
solution = [[]]
nums_set = set(num)
for index in range(len(num)):
    solution = [i + [j] for i in solution for j in nums_set.difference(set(i))]
    print(solution)

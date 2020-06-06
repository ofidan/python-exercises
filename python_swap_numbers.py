my_list = [23, 4, 243, 43, 56, 12, 5, 26, 40]
swapped = True
while swapped:
    swapped = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i + 1]:
            my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
            swapped = True
            
print(my_list)
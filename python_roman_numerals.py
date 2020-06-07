# Symbol       Value
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3

# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

num=int(input("Please input a number: "))
if num < 1 or num > 3999:
    print("the input number is out of range")
else:
    rom_num=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    digits=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result=[]
    i=0
    while i < len(digits):
        if num>=digits[i]:
            result.append(rom_num[i])
            num -= digits[i]
        else:
            i += 1
result="".join(result)
print(result)


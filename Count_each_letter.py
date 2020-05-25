# input = ("hippo runs to us!") 
# output: {'s': 2, 'r': 1, 't': 1, 'h': 1, 'n': 1, 
# 'i': 1, 'u': 2, 'o': 2, 'p': 2, ' ': 3, '!': 1}

sentence = input("Enter a sentence with lowercase letters: ")
# sentence = "hippo runs to us!"
counted_letters = {}
for i in sentence:
    counted_letters[i] = sentence.count(i)
print(counted_letters)


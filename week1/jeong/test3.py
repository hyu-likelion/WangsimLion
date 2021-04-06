word = input()
word = word.upper()
tmpList = list(word)
dictionary = {}
for s in tmpList:
    if s in dictionary:
        dictionary[s] += 1
    else:
        dictionary[s] = 1
#print(dictionary)
result = [k for k, v in dictionary.items() if max(dictionary.values()) == v]
if len(result) > 1:
    print('?')  
else:
    print(result[0])


word = input().lower()
s1 = set(word)

dic = {}

def get_key(val):
    for key, value in dic.items():
         if val == value:
             return key

for s in s1 :
    letCnt = word.count(s)
    dic[s]=letCnt

cnts = list(dic.values())

max = max(cnts)

maxCount = cnts.count(max)

if maxCount == 1 :
    print(get_key(max).upper())
else :
    print("?")
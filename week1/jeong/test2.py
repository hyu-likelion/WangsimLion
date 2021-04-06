num = int(input())
mainList = []
for i in range(num):
    inputList = list(map(int, input().split()))
    mainList.append(inputList)
for i in range(num):

    tmpList = mainList[i]
    listNum = tmpList[0]
    del tmpList[0]
    average = sum(tmpList) / listNum
    overNum = 0
    for j in tmpList:
        if (j > average):
            overNum += 1

    print(format(overNum / listNum * 100, ".3f") +'%')
    

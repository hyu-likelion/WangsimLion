cnt = int(input())
answers = []

for _ in range(cnt):
    nums = list(map(int,input().split(" ")))
    sum = 0
    count = nums[0]
    del nums[0]

    for num in nums :
        sum = sum + num

    ave = sum/count

    exceedAve = 0
    for num in nums :
        if num > ave :
            exceedAve = exceedAve + 1
    
    answer = exceedAve/count*100
    answers.append(answer)

for answer in answers:
    print("{:.3f}%".format(answer))

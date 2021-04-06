def average(score) :
    #score값 다 더해서 - score[0]
    score_average = (sum(score) - score[0]) / score[0]
    del score[0]
    student = []
    for i in score :
        if i > score_average :
            student.append(i)
    a = round((len(student) / len(score)) * 100 , 3) #평균 이상 학생 비율
    return a #셋쨋자리 반올림

c = int(input()) #테스트 케이스
i = 0
while i < c :
    score = list(map(int, input().split()))
    print(str(average(score))+"%")
    i += 1
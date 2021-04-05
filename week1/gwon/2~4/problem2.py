cnt = int(input())                              # 테스트 케이스의 개수 C입력
answers = []                                    # 정답을 답을 리스트 생성

for _ in range(cnt):                            # C의 개수만큼 반복
    nums = list(map(int,input().split(" ")))    # 공백으로 구분한 후 int값으로 바꿔 nums 배열에 입력
    sum = 0                                     # sum 초기화
    count = nums[0]                             # 학생의 수를 count 변수에 입력
    del nums[0]                                 # 학생 수 리스트에서 제거

    for num in nums :                           
        sum = sum + num                         # 학생 점수들의 합 구하기

    ave = sum/count                             # 평균 구하기

    exceedAve = 0                               # 평균 넘는 학생의 수를 구하기 위한 
    for num in nums :                           
        if num > ave :                          # 학생 점수가 평균을 넘는지 확인
            exceedAve = exceedAve + 1           # 넘으면 exceedAve 값을 1 올려준다
    
    answer = exceedAve/count*100                # 넘는 학생의 비율을 구해준 후 퍼센트값으로 출력하기 위해 *100
    answers.append(answer)                      # answer 배열에 추가

for answer in answers:
    print("{:.3f}%".format(answer))             # format 함수를 이용해 문자열에 소수점 셋째자리까지 출력

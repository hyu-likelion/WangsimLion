a,b = input().split(" ")    # 숫자를 공백으로 구분해 a,b에 입력 받기
aR = int(a[::-1])           # 문자열을 뒤집은 후 숫자로 바꾸기
bR = int(b[::-1])

if aR > bR :                # 크기 비교 후 출력
    print(aR)
else :
    print(bR)
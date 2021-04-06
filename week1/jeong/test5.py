def solution(phone_book):
    phone_book.sort(key = len) #길이순으로 오름차순으로 정렬
    compList = []
    flag = True
    for phone in phone_book:
        if not compList:
            compList.append(phone_book[0]) #처음 시작할때만 적용
        else:
            for comp in compList:
                temp = phone[0:len(comp)] #phone의 길이를 비교대상만큼 자르기
                if temp == comp: #접두어인지 확인
                    flag = False #접두어가 있는 경우 플래그 변화
            if flag == False:
                break
            else: #접두어가 없어서 compare for 문을 다 돌았을 때도 여전히 true
                compList.append(phone) #새로운 접두어로 추가

    return flag

def main():
    phone_book = ["12","123","1235","567","88"]
    print(solution(phone_book))
main()
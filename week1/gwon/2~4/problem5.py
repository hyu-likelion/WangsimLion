def solution(phone_book):
    minNum = len(phone_book[0])                         # 가장 짧은 번호의 길이를 구하기 위해 초기화
    
    for num in phone_book:                              # 가장 짧은 번호의 길이를 구해서 minNum에 넣기
        if minNum > len(num) :
            minNum = len(num)
    
    for index in range(len(phone_book)):                # 가장 짧은 번호의 길이만큼 모든 번호 짜르기
        phone_book[index] = phone_book[index][:minNum]
    
    s1 = set(phone_book)                                # 중복을 제거해주기 위해 집합으로 만들기 s1과 phone_book의 요소의 개수가 같으면 중복되는 번호가 없는 것
    return len(s1)==len(phone_book)

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
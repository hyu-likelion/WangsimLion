def solution(phone_book):
    check = phone_book[0]
    del phone_book[0]
    length = len(check)
    answer = True

    for num in phone_book :
        if check == num[:length]:
            answer = False
    return answer


print(solution(["119", "97674223", "1195524421"]))
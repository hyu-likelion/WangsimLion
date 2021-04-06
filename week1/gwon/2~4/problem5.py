phone_book = ["123", "456", "789"]
phone_book2 = ["12", "123", "1235", "567", "88"]
phone_book3 = ["119", "97674223", "1195524421"]



def solution(phone_book):
    phone_book.sort()
    
    # 바로 뒤와 비교
    # 오름차순 정렬되어 있으므로 어차피 바로 뒤에 것에 포함되어 있지 않으면 가망이 없다.
    for i in range(len(phone_book) - 1):
        val = phone_book[i]
        compared_val = phone_book[i+1]
        if val == compared_val[:len(val)]:
            return False
    return True

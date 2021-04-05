word = input().upper()              # 단어를 word 변수에 입력 받고 전부 대문자로 변경 ex) Mississipi -> MISSISSIPI
s1 = set(word)                      # 중복을 제거하기 위한 집합 s1 생성  ex) (M,I,S,P)

dic = {}                            # 비어 있는 딕셔너리 생성

def get_key(val):                   # 밸류값으로 키값을 찾는 함수
    for key, value in dic.items():
         if val == value:
             return key

for s in s1 :                       # s1에 있는 문자들이 word에 몇개 들어있는지 체크
    letCnt = word.count(s)          # count 함수를 사용 ex) letCnt = word.count("M") = 1
    dic[s]=letCnt                   # 딕셔너리에 키값과 밸류값으로 문자와 문자 개수 입력 ex ) { "M" : 1 }
                                    # {'I': 4, 'M': 1, 'S': 4, 'P': 1}

cnts = list(dic.values())           # dic에서 문자개수들을 리스트로 뽑기 ex) [4,1,4,1]

max = max(cnts)                     # 문자 개수들 중 가장 큰 값 찾기  ex) max = 4

maxCount = cnts.count(max)          # 가장 많이 나온 문자가 여러개인지 확인 ex) maxCount = 2

if maxCount == 1 :                  # 가장 많이 나온 문자가 하나일 경우 문자 출력 
    print(get_key(max))             
else :                              # 여러개일 경우 물음표 출력
    print("?")
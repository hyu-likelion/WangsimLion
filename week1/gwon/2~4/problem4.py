def solution(participant, completion):
    for com in completion:                  # 완주한 배열에 있는 사람들 하나씩 빼오기
        if com in participant:              # 그 사람이 참가자 명단에 있는지 확인
            participant.remove(com)         # 있으면 참가자 명단에서 제거해주기
    answer = participant[0]                 # 완주하지 못한 사람을 리턴하기
    return answer
def solution(participant, completion):
    for com in completion:
        if com in participant:
            participant.remove(com)
    answer = participant[0]
    return answer
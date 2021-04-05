def solution(participant, completion):
    for a in completion :
        if a in participant :
            participant.remove(a)
    answer=participant[0]
    return answer

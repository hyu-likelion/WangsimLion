def solution(participant, completion):
    for c in completion :
        if c in participant :
            participant.remove(c)
    answer = participant[0]
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
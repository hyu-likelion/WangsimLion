def solution(participant, completion):
    for p in completion:
        if p in participant:
            participant.remove(p)
    answer = participant[0]
    return answer

def main():
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    answer = solution(participant, completion)
    print(answer)

main()
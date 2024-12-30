def solution(arr, k):
    set_list = set()
    answer = []
    for i in arr:
        if i not in set_list:
            answer.append(i)
            set_list.add(i)
    num = len(answer)
    if num < k:
        answer.extend([-1] * (k - num))
    return answer[:k]


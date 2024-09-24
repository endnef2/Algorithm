def solution(array):
    a = set(array)
    cnt_list = []
    for i in a:
        cnt_list.append((array.count(i), i)) 
    cnt_list = sorted(cnt_list, reverse=True)
    if len(cnt_list)>1:
        if cnt_list[0][0] == cnt_list[1][0]:
            answer = -1
        else:
            answer = cnt_list[0][1]
    else:
        answer = cnt_list[0][1]
    return answer
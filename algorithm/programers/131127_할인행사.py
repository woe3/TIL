def solution(want, number, discount):
    answer = 0
    want_dic = {}
    total_num = 0
    for item, num in zip(want, number):
        want_dic[item] = num
        total_num += num

    end_point = len(discount) - 9

    for cnt in range(0, end_point):
        total_num_copy = total_num
        want_dic_copy = want_dic.copy()
        for i in range(cnt, cnt + 10):

            if discount[i] in want_dic_copy and want_dic_copy[discount[i]] > 0:
                want_dic_copy[discount[i]] -= 1
                total_num_copy -= 1

        if total_num_copy == 0:
            answer += 1

    return answer
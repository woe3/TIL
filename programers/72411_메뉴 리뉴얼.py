def solution(orders, course):
    answer_temp = [[] for _ in range(course[-1]+1)]
    
    length = len(orders)
    course_max = [0] * (course[-1]+1)
    for i in range(length):
        menu_1 = set(orders[i])
        for j in range(i+1, length):
            menu_2 = set(orders[j])
            menu = menu_1 & menu_2
            if len(menu) in course:
                
                menu = list(menu)
                menu.sort()
                menu_str = "".join(menu)
                if menu_str in answer_temp[len(menu)]:
                    continue
                count = 0
                for k in orders:
                    count_if_in = 0
                    for l in menu:
                        if l in k:
                            count_if_in += 1

                    if count_if_in == len(menu):
                        count += 1

                if count == course_max[len(menu)]:
                    answer_temp[len(menu)].append(menu_str)
                elif count > course_max[len(menu)]:
                    course_max[len(menu)] = count
                    answer_temp[len(menu)] = []
                    answer_temp[len(menu)].append(menu_str)

    answer = []
    for i in answer_temp:
        answer += i
    answer.sort()
    return answer
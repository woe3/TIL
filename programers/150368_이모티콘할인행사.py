from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    for discount in product([0.9, 0.8, 0.7, 0.6], repeat=len(emoticons)):
        temp_answer = [0, 0]
        for user in users:
            buy = 0
            for i in range(len(discount)):
                if 100 - discount[i]*100 >= user[0]:
                    buy += discount[i]*emoticons[i]
            if buy >= user[1]:
                temp_answer[0] += 1
            else:
                temp_answer[1] += buy
        if temp_answer[0] > answer[0]:
            answer = temp_answer
        elif (temp_answer[0] == answer[0] and
        temp_answer[1] > answer[1]):
            answer = temp_answer
                     
    
    
    return answer

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
solution(users, emoticons)

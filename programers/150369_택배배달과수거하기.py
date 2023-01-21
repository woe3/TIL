def solution(cap, n, deliveries, pickups):
    answer = 0
    d = n-1
    p = n-1
            
    while d >= 0 or p >= 0:
        temp_answer = 0
        del_cap = cap
        pick_cap = cap
        # 뒤에서부터 순회한다. 배달 상자가 있다면 배달 가능 한 만큼 빼주고
        # 더 배달 가능하면 다음 배달 할 곳을 찾는다.
        # for문이 -1까지 도는 이유는 리스트에 마지막으로 돌아가서 종료 조건을 만들어 주기 위함이다.
        for house in range(d,-2,-1):
            if deliveries[house] == 0:
                d = house
                continue
            else:
                if house+1 > temp_answer:
                    temp_answer = house+1
            if deliveries[house] > del_cap:
                deliveries[house] -= del_cap
                d = house
                break
            else: 
                del_cap -= deliveries[house]
                deliveries[house] = 0
                
                
        for house in range(p,-2,-1):
            if pickups[house] == 0:
                p = house
                continue
            else:
                if house+1 > temp_answer:
                    temp_answer = house+1
            if pickups[house] > pick_cap:
                pickups[house] -= pick_cap
                p = house
                break
            else: 
                pick_cap -= pickups[house]
                pickups[house] = 0
        answer += temp_answer*2
    return answer
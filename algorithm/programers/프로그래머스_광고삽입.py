import heapq

def time_to_sec (log):
    log = log.split("-")
    log[0] = list(map(int, log[0].split(":")))
    log[1] = list(map(int, log[1].split(":")))
    sec = []

    for i in range(1,-1,-1):
        temp = 0
        for j in range(3):
            temp += (log[i][j] * (60**(2-j)))

        sec.append(temp)
    return sec

def sec (a):
    a = list(map(int, a.split(":")))
    sec = []

    temp = 0
    for j in range(3):
        temp += (a[j] * (60**(2-j)))

    sec.append(temp)
    return sec

def solution(play_time, adv_time, logs):
    answer = ''
    answer_time = 0
    play_time = sec(play_time)
    adv_time = sec(adv_time)
    if play_time < adv_time:
        return "00:00:00"
    
    logs_sec = []
    for i in logs:
        heapq.heappush(logs_sec, time_to_sec(i))
    
    while logs_sec:
        temp = 0
        log = heapq.heappop(logs_sec)        
        if log[0] > log[1] + adv_time:
            temp += adv_time
        else: temp += log[1] - log[0]
        for i in range(len(logs_sec)):
            if logs_sec[0][1]
        
    return answer


def solution(fees, records):
    answer = []
    temp_answer = []
    time_stamp = {}
    for i in records:
        info = i.split(" ")
        time = list(map(int, info[0].split(":")))
        time_minute = time[0] * 60 + time[1]
        car_number = info[1]
        car_status = info[2]
        if car_status == "IN":
            time_minute *= -1
        
        if car_number in time_stamp:
            time_stamp[car_number].append(time_minute)
        else:
            time_stamp[car_number] = [time_minute]
            
    for key in time_stamp.keys():
        val = time_stamp[key]
        time_to_pay = sum(val)
        if len(val) % 2:
            time_to_pay += (23 * 60 + 59)
        time_to_pay -= fees[0]
        payment = fees[1]
        if time_to_pay > 0:
            payment += ((time_to_pay -1) // fees[2] + 1) * fees[3]
        
        temp_answer.append([int(key), payment])
    temp_answer.sort(key = lambda x : x[0])
    for i in temp_answer:
        answer.append(i[1])
    return answer
def play_time(times):
    start = times[0].split(":")
    end = times[1].split(":")

    start_min = int(start[0]) * 60 + int(start[1])
    end_min = int(end[0]) * 60 + int(end[1])
    if end_min < start_min:
        end_min += 24 * 60
    return end_min - start_min + 1


def solution(m, musicinfos):
    answer = "(None)"
    answer_length = 0
    memory = []
    cnt = 0
    while cnt < len(m):
        temp = ""
        temp += m[cnt]
        cnt += 1
        if cnt < len(m) and m[cnt] == "#":
            temp += m[cnt]
            cnt += 1
        memory .append(temp)
    print(memory)
    for i in musicinfos:
        musicinfo = i.split(",")
        playtime = play_time(musicinfo)
        print(playtime)

        #멜로디 만들기
        melody = []
        i = 0
        while i < playtime:
            temp = ""
            index = i % len(musicinfo[3])
            temp += musicinfo[3][index]
            i += 1
            index = i % len(musicinfo[3])
            if musicinfo[3][index] == "#":
                temp += musicinfo[3][index]
                i += 1
                playtime += 1
            melody.append(temp)

        print(melody)
        print()

        #멜로디 찾기
        end = len(melody) - len(memory)+1
        for s in range(end):
            if (melody[s:s+len(memory)] == memory
                    and len(melody) > answer_length):
                answer = musicinfo[2]
                answer_length = len(melody)

    return answer
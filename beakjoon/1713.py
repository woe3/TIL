import sys
n = int(sys.stdin.readline())
r = int(sys.stdin.readline())
recomand = list(map(int, sys.stdin.readline().split()))

picture = {}
for i in range(r):
    if recomand[i] in picture:
        picture[recomand[i]][0] += 1        
    elif len(picture) < n:
        picture[recomand[i]] = [1, i]
    elif len(picture) == n:
        num = 1001
        delete_pic = 0
        for key in picture:
            if num > picture[key][0]:
                delete_pic = key
                num = picture[key][0]
            elif num == picture[key][0]:
                if picture[delete_pic][1] > picture[key][1]:
                    delete_pic = key
            print(num)
        del picture[delete_pic]
        picture[recomand[i]] = [1, i]
    

answer = [key for key in picture]
answer.sort()
for i in answer:
    print(i, end = " ")
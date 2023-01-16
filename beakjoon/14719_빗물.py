import sys
h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))


visited = [0] * w
answer = 0
for height in range(h, 0, -1):
    temp_list = []
    for block_index in range(w):
        if blocks[block_index] >= height and not visited[block_index]:
            temp_list.append(block_index)
        
    if len(temp_list) > 1:
        for i in range(len(temp_list)-1):
            for j in range(temp_list[i]+1, temp_list[i+1]):
                if not visited[j]:
                    answer += height - blocks[j]        
                    visited[j] = 1
    print(temp_list)
    print(answer)
    print(visited)
print(answer)
        
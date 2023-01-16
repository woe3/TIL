import sys
h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))

# 블럭 개수 만큼 방문 기록을 남길 리스트 생성
visited = [0] * w
answer = 0
# 가장 높은 블럭부터 내려가면서 2개 이상 있는지 확인
for height in range(h, 0, -1):
    temp_list = []
    for block_index in range(w):
        if blocks[block_index] >= height and not visited[block_index]:
            temp_list.append(block_index)
    # 두개 이상 있다면 물이 담길수 있다는 뜻
    if len(temp_list) > 1:
        for i in range(len(temp_list)-1):
            for j in range(temp_list[i]+1, temp_list[i+1]):
                # 방문되지 않았다면 정답에 더하기
                if not visited[j]:
                    answer += height - blocks[j]        
                    visited[j] = 1

print(answer)
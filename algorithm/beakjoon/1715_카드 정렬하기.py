import sys
import heapq

n = int(sys.stdin.readline())
priority_queue = []
for _ in range(n):
    card = int(sys.stdin.readline())
    heapq.heappush(priority_queue, card)

answer = 0
while len(priority_queue) > 2:
    card_1 = heapq.heappop(priority_queue)
    card_2 = heapq.heappop(priority_queue)
    temp_answer = card_1 + card_2
    answer += temp_answer
    heapq.heappush(priority_queue, temp_answer)

print(sum(priority_queue) + answer)
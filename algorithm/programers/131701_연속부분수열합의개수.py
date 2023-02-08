from collections import deque
def solution(elements):
    answer = 0
    elements = deque(elements)
    answer_set = set()

    for i in range(1, len(elements)+1):
        for j in range(1, len(elements) + 1):
            sequence = deque()
            temp_element = elements.copy()
            while len(sequence) < i:
                if not temp_element:
                    break
                temp = temp_element.popleft()
                if not sequence:
                    sequence.append(temp)
                elif sequence[-1] > temp:
                    break
            if len(sequence) == i:
                answer_set.add(sum(sequence))
                print(sequence)

            sequence = deque()
            temp_element = elements.copy()
            while len(sequence) < i:
                if not temp_element:
                    break
                temp = temp_element.pop()
                if not sequence:
                    sequence.append(temp)
                elif sequence[-1] > temp:
                    break
            if len(sequence) == i:
                answer_set.add(sum(sequence))
                print(sequence)
            elements.append(elements.popleft())

    return len(answer_set)

print(solution([7,9,1,1,4]))
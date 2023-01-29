import sys

sys.setrecursionlimit(10**4)
nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

graph ={}

def create_tree(nums):
    global graph
    end = len(nums)
    graph[nums[0]] = [None, None]
    if len(nums) == 1:
        return
    else:
        for i in range(1, end):
            if nums[0] < nums[i]:
                graph[nums[0]][1] = nums[i]
                end = i
                break
        for j in range(1, end):
            if nums[0] > nums[j]:
                graph[nums[0]][0] = nums[j]
                break
        if nums[1:end]:
            create_tree(nums[1:end])
        if nums[end:]:
            create_tree(nums[end:])



def postorder(graph, root):
    if not root == None:
        postorder(graph, graph[root][0])
        postorder(graph, graph[root][1])
        print(root)


create_tree(nums)
postorder(graph, nums[0])
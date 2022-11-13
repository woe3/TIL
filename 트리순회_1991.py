import sys
from collections import deque
# A~Z = 65~90

n = int(sys.stdin.readline())
alphabet = {}
for _ in range(n):
    p, lc, rc = sys.stdin.readline().split()
    alphabet[p] = [lc, rc]

#전위 순회
def preorder(root):
    if not root == '.':
        print(root, end = '')
        preorder(alphabet[root][0])
        preorder(alphabet[root][1])

#중위 순회
def inorder(root):
    if not root == '.':
        inorder(alphabet[root][0])
        print(root, end = '')
        inorder(alphabet[root][1])

#후위 순회
def postorder(root):
    if not root == '.':
        postorder(alphabet[root][0])
        postorder(alphabet[root][1])
        print(root, end = '')



preorder('A')
print()
inorder('A')
print()
postorder('A')

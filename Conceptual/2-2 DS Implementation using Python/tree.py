class Node:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None

def main():
    v = int(input())
    root = Node(v)
    q = []
    q.append(root)
    while len(q) != 0:
        p = q[0]
        q.pop(0)
main()
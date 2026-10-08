"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def depth(node):
            ans = 0
            while node:
                ans+=1
                node = node.parent
            return ans

        p_d, q_d = depth(p), depth(q)

        while p_d > q_d:
            p = p.parent
            p_d -= 1
            

        while q_d > p_d :
            q = q.parent
            q_d -= 1

        while p != q:
            p = p.parent
            q = q.parent

        return p
        
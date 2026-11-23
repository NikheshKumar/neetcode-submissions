"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n,r,c):
            if n==1:
                return Node(bool(grid[r][c]),True)
            while n:
                n = n//2
                tl = dfs(n,r,c)
                tr = dfs(n,r,c+n)
                bl = dfs(n,r+n,c)
                br = dfs(n,r+n,c+n)

                if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val==tr.val==br.val==bl.val):
                    return tl

                else:
                    return Node(False,False,tl,tr,bl,br)

            
        return dfs(len(grid),0,0)


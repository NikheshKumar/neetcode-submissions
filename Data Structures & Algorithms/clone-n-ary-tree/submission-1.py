"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        def dfs(node):
            if not node:
                return
            ch = [dfs(c) for c in node.children]
            new = Node(node.val)
            new.children = ch
            return new

        return dfs(root)
        
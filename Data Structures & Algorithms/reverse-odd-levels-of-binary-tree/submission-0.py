# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def bfs(node):
            if not node:
                return node

            q = deque([node])
            level = 0

            while q:
                level_nodes = [q.popleft() for _ in range(len(q))]
                if level % 2:
                    i, j = 0, len(level_nodes)-1
                    while i < j:
                        level_nodes[i].val, level_nodes[j].val = level_nodes[j].val, level_nodes[i].val
                        i += 1
                        j -= 1

                for curr in level_nodes:
                    if curr.left : q.append(curr.left)
                    if curr.right : q.append(curr.right)

                level += 1

            return node

        return bfs(root)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def bfs(node):
            nonlocal ans
        
            if not node:
                return ans

            q = deque([node])

            while q:
                level = []
                level_size = len(q)
                for _ in range(level_size):
                    curr = q.popleft()
                    if curr.left : q.append(curr.left)
                    if curr.right : q.append(curr.right)
                    level.append(curr.val)

                ans.append(level[-1])

            return ans


        return bfs(root)



        
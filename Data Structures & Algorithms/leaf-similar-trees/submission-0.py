# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:

        ans = []
        def dfs(node, ans):
            if node is None:
                return
            
            if not node.left and not node.right:
                ans.append(node.val)

            dfs(node.left, ans)
            dfs(node.right, ans)

            return ans


        ans1, ans2 = [], []
        return dfs(root1, ans1)==dfs(root2, ans2)
        
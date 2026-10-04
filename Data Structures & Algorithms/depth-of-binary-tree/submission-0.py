# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def f(root):
            if not root:
                return 0
            return max(f(root.left)+1, f(root.right)+1)

        ans = f(root)
        return ans
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        def dfs(node, depth):
            nonlocal ans
            if not node:
                return ans

            if depth==len(ans):
                ans.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

            return ans
            


        return dfs(root, 0)

            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def minNode(node):
            curr = node
            while curr and curr.left:
                curr = curr.left

            return curr

        
        def dfs(node, val):
            if not node:
                return

            if val > node.val:
                node.right = dfs(node.right, val)
            
            elif val < node.val:
                node.left = dfs(node.left, val)

            
            else:

                if not node.right:
                    return node.left
                
                elif not node.left:
                    return node.right

                else:
                    m = minNode(node.right)
                    node.val = m.val
                    node.right = dfs(node.right, m.val)

            
            return node


        return dfs(root, key)
        
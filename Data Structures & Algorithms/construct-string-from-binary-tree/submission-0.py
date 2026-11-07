# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(root):
            ans = []
            stack = [(root,0)]
            while stack:
                node, curr = stack.pop()

                if curr == 0 :
                    ans.append(str(node.val))
                    if node.left or node.right:
                        ans.append("(")
                        stack.append((node,1))
                        if node.left:
                            stack.append((node.left,0))

                elif curr == 1:
                    ans.append(")")
                    if node.right:
                        ans.append("(")
                        stack.append((node,2))
                        stack.append((node.right,0))

                elif curr == 2:
                    ans.append(")")

            return "".join(ans)

        ans = dfs(root)
        return ans




        
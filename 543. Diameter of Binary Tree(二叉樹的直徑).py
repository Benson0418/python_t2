# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            l=dfs(root.left)
            r=dfs(root.right)
            deapth=max(l,r)+1
            res=max(res,l+r)
            return deapth
        dfs(root)
        return res
            

            

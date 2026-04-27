# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, i, res):
            if not root:
                return
            inorder(root.left, i, res)
            if i[-1] == k:
                res[-1] = root.val
            i[-1] += 1
            inorder(root.right, i, res)
        
        i, res = [1], [-1]
        inorder(root, i, res)
        return res[-1]
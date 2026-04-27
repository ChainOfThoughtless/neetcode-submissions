# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findPathSum(root, targetSum, pathSum):
            if not root:
                return False
            val = root.val if len(pathSum) == 0 else (root.val + pathSum[-1])
            pathSum.append(val)
            if not root.left and not root.right and pathSum[-1] == targetSum:
                return True
            if findPathSum(root.left, targetSum, pathSum):
                return True
            if findPathSum(root.right, targetSum, pathSum):
                return True
            pathSum.pop()
            return False
        return findPathSum(root, targetSum, [])
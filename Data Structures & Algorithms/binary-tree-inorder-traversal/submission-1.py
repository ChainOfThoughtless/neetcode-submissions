# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        bt, res, visited = [], [], set()
        bt.append(root)
        while len(bt) > 0:
            curr = bt.pop()
            if not curr:
                continue
            if curr.left and curr.left.val not in visited: #go left
                bt.append(curr)
                bt.append(curr.left)
                curr = curr.left
            else: #print curr, push right
                res.append(curr.val)
                visited.add(curr.val)
                if curr.right:
                    bt.append(curr.right)
        return res
        #bt: 
        #res: 2,4,1,5,3
        
        
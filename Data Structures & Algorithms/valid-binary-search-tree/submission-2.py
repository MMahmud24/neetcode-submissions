# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = [[]]
        is_valid = [True]
        def in_order(root):
            if not root or not is_valid[0]:
                return

            in_order(root.left)
            if res[0]:
                if not (res[0][-1] < root.val):
                    is_valid[0] = False
            res[0].append(root.val)
            in_order(root.right)

        in_order(root)

        return is_valid[0]
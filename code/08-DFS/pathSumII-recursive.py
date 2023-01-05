import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        self.results = []

        def depth_first_search(node, currSum, tarSum, bt):

            if node is None: return

            bt.append(node.val)

            currSum += node.val
            if node.left is None and node.right is None and currSum == tarSum: 
                self.results.append(copy.deepcopy(bt))


            depth_first_search(node.left, currSum, tarSum, bt)
            depth_first_search(node.right, currSum, tarSum, bt)
            bt.pop(-1)

        if root is None: return []
        bt = []
        depth_first_search(root, 0, targetSum, bt)
        return self.results

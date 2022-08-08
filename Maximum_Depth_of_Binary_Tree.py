"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def maxDepth(self, root):
        way_list = []
        depth = 0
        max_depth = 0
        count = 0
        
        pass
        
testcase = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(testcase.maxDepth(root))
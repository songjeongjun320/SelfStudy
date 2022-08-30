"""
Given the root of a binary tree, return the 
inorder traversal of its nodes' values.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def inorderTraversal(self, root):
        return inorderTraversal(self, root.left)
    
root = TreeNode(1,None,TreeNode(2,TreeNode(3)))
testcase = Solution()
print(testcase.inorderTraversal(root))
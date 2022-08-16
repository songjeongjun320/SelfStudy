"""
Given the root of a binary tree, return the 
inorder traversal of its nodes' values.
"""

from asyncio.windows_events import NULL


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def inorderTraversal(self, root):
        
        
        pass
    
root = [1,NULL,2,3]
testcase = Solution()
print(testcase.inorderTraversal(root))
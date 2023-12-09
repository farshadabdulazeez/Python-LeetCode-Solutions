# 94. Binary Tree Inorder Traversal

'''

Given the root of a binary tree, return the inorder traversal of its nodes' values.

'''

# Solution

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return (
        self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    ) if root else []
        
        
'''

# Approach

'''

Base Case:

If the root is None, indicating an empty subtree, an empty list [] is returned.
Recursive Calls:

The function makes two recursive calls:
self.inorderTraversal(root.left): Recursively traverses the left subtree.
self.inorderTraversal(root.right): Recursively traverses the right subtree.
Concatenation:

The result of the left subtree, the value of the current node ([root.val]), and the result of the right subtree are concatenated using the + operator.
Final Result:

The final result is the inorder traversal of the binary tree.

Time complexity : 0(n)

Space complexity : 0(n)
'''
# 606. Construct String from Binary Tree

'''

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

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
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        result = [str(root.val)]
        
        if root.left or root.right:
          result.append("({})".format(self.tree2str(root.left)))
      
        if root.right:
          result.append("({})".format(self.tree2str(root.right)))
        
        return ''.join(result)



'''

# Approach

'''

Base Case:

If the given root is None, return an empty string.
Recursive Construction:

Construct the string representation of the current node's value.
If the node has a left child or a right child, recursively construct the string representations of the left and right subtrees.
Use parentheses to enclose the left and right subtrees only if they exist.
Joining Results:

Join the constructed substrings to form the final result.

Time compplexity : 0(n)

Space complexity : 0(h) where h is the height of the binary tree

'''
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
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
        
        
'''

# Approach

'''

Initialize an Empty Stack and Current Node:

We start with an empty stack and the current node set to the root of the binary tree.
Iterate until the Stack is Empty and Current Node is None:

We use a while loop that continues until both the stack is empty and the current node is None.
Inside the loop, we traverse to the leftmost node by pushing nodes onto the stack.
Push Left Nodes onto the Stack:

While the current node is not None, we keep pushing the current node onto the stack and move to its left child.
Pop Nodes from the Stack:

Once we reach the leftmost node, we pop nodes from the stack, append their values to the result list, and move to their right child.
Continue Iterating:

We continue this process until the stack is empty and the current node is None.

Time complexity : 0(n)

Space complexity : 0(n)
'''
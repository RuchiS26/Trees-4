# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : yes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        # variable to store LCA node.
        self.res = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # if its a end of a branch
            if not current_node:
                return False

            # left Recursion
            left = recurse_tree(current_node.left)

            # right Recursion
            right = recurse_tree(current_node.right)

            # if the current node is one of p or q
            mid = current_node == p or current_node == q

            # if any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.res = current_node

            # return true if either of the three values is True.
            return mid or left or right

        # traverse the tree
        recurse_tree(root)
        return self.res

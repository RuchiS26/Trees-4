# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # value of p
        p_val = p.val

        # value of q
        q_val = q.val

        # start from the root node of the tree
        node = root

        # traverse the tree
        while node:

            # value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                # if both p and q are greater than parent
                node = node.right

            elif p_val < parent_val and q_val < parent_val:
                # if both p and q are lesser than parent
                node = node.left

            else:
                # we have found the split point, i.e. the LCA node.
                return node

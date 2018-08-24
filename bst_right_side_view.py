 Binary Tree Right Side View
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        if root.left == root.right == None:
            return [root.val]
        
        right_side_view = []
        
        level_nodes = [root]
        right_side_view.append(root.val)
        
        while level_nodes:
            next_level_values = []
            next_level_nodes = []
            for node in level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                    next_level_values.append(node.left.val)
                if node.right:
                    next_level_nodes.append(node.right)
                    next_level_values.append(node.right.val)
            level_nodes = next_level_nodes
            if next_level_values:
                right_side_view.append(next_level_values[-1])
        return right_side_view
        

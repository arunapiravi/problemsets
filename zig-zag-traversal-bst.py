Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        values = []
        if root == None:
            return values
        
        # perform a breadth-first traversal, store the order
        level = []
        level.append(root)
        values.append([root.val])
        left_to_right = True
        while level:
            next_level = []
            next_level_values = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                    next_level_values.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    next_level_values.append(node.right.val)
            level = next_level
            if next_level_values:
                values.append(next_level_values)
                
        # alternate the order-reversal of level nodes
        for index, value in enumerate(values):
            if index % 2:
                values[index] = value[::-1]
        return values
    

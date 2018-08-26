"""
Flatten Binary Tree to Linked List
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""


def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        linked = []
				
        def __flatten(root, linked):
            if root != None:
                linked.append(root)
                __flatten(root.left, linked)
                __flatten(root.right, linked)
        
        __flatten(root, linked)
        
        if linked:
            head = linked[0]
            head.left = None
            prev = head
        for node in linked[1:]:
            prev.right = node
            node.left = None
            prev = node




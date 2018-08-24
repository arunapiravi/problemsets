109. Convert Sorted List to Binary Search Tree
DescriptionHintsSubmissionsDiscussSolution
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = self.convert_list_to_array(head)
        print arr
        return self.build_BST(arr)
    
    def build_BST(self, array):
        if len(array) == 0:
            return None
        mid = (len(array)-1)/2
        root = TreeNode(array[mid])
        root.left = self.build_BST(array[:mid])
        root.right = self.build_BST(array[mid+1:])
        return root
        
    def convert_list_to_array(self, head):
        if head == None:
            return []
        array = []
        pos = head
        while pos:
            array.append(pos.val)
            pos = pos.next
        return array
        

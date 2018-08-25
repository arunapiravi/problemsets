"""
Construct Binary Tree from Inorder and Postorder Traversal
DescriptionHintsSubmissionsDiscussSolution
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(postorder) ==0:
            return None
        j = inorder.index(postorder[-1])
        root = TreeNode(postorder.pop())
        root.left = self.buildTree(inorder[:j], postorder[:j])
        root.right = self.buildTree(inorder[j+1:], postorder[j:])
        return root
        

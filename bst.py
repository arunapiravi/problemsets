class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, element):
		"""
		O(logN)
		"""
		if self.root == None:
			self.root = TreeNode(element)
		else:
			self.__insertNode(self.root, element)

	def __insertNode(self, root, element):
		if root == None:
			root = TreeNode(element)
			print "element {0} inserted".format(element)
		elif element > root.val:
			root.right = self.__insertNode(root.right, element)
		else:
			root.left = self.__insertNode(root.left, element)
		return root


	def delete(self, element):
		"""
		O(logN) 
		"""
		self. __delete(self.root, element)

	def __delete(self, root, element):
		"""
		O(logN)
		"""
		if root == None:
			return None		

		if root.val > element:
			root.right = self.__delete(root.right, element)
		
		elif root.val < element:
			root.left =  self.__delete(root.left, element)

		else:
			# Element exists
			if root.right == None:
				return root.left

			elif root.left == None:
				return root.right

			# we have both children
			temp = root.right
			while temp.left != None:
				temp = temp.left
			root.val = temp.val
			print "Deleting element {0}".format(element)
			root.right = self.__delete(root.right, root.val)
		return root
				
	
	def search(self, element):
		"""
		O(logN)
		"""
		return self.__search(self.root, element)
	
	def __search(self, root, element):
		"""
		O(logN)
		"""
		if root == None:
                        # no tree
			print "element {0} not found".format(element)
                        return None

		if root.val == element:
			print "element {0} found".format(element)
			return root

                elif element < root.val:
                         return self.__search(root.left, element)

                else:
                         return self.__search(root.right, element)


	#### All traversals are O(N) because they traverse all nodes in the tree
	
	def inorder(self):
		print "Inorder traversal :"
		self.__inorder(self.root)

	def __inorder(self, root):
		if root == None:
			return None
		else:
			self.__inorder(root.left)
			print root.val
			self.__inorder(root.right)

	def inorderTraversal(self, root):
    		"""
		Iterative inorder traversal
		"""
		ans = []
    		stack = []
    
   		while stack or root:
        		if root:
            			stack.append(root)
            			root = root.left
        		else:
            			tmpNode = stack.pop()
            			ans.append(tmpNode.val)
            			root = tmpNode.right
    		return ans


	def preorder(self):
		self.__preorder(self.root)

	def __preorder(self, root):
		if  root!= None:
			print root.val
			self.__preorder(root.left)
			self.__postorder(root.right)


	def postorder(self):
		self.__postorder(self.root)

	def __postorder(self, root):
		if root != None:
			self.__postorder(root.left)
			self.__postorder(root.right)
			print root.val
	
	def levelorder(self):
		"""
		O(N) Breadth-first traversal
		returns [[root.val],[root.left.val, root.right.val]]
		all level nodes grouped in a single list
		"""
			
		def __levelorder(root):
        		"""
        		:type root: TreeNode
        		:rtype: List[List[int]]
        		"""
        		result = []
        		if not root:
            			return result
        		level = [root]
        		while level:
            			child_values = []
            			next_level = []
            			for node in level:
                			child_values.append(node.val)
                			if node.left:
                    				next_level.append(node.left)
                			if node.right:
                    				next_level.append(node.right)
            			level = next_level
            			result.append(child_values)
       			return result
		print __levelorder(self.root)

	def depth_first_traversal(self):
		"""
		O(N)
		"""
		def __depthfirst(root, path):
			if root == None:
				return
			path.append(root.val)
			if root.left == root.right == None:
				print path
				path.pop()
			else:
				__depthfirst(root.left, path)
				__depthfirst(root.right, path)
		
		path = []
		__depthfirst(self.root, path)
				
	
	def get_depth(self, node):
		"""
		O(N) because traversal of both left 
		and right subtrees is required
		"""
		if node == None:
			return 0
		if node.left == node.right == None:
			return 1
		return 1 + max(self.get_depth(node.left), self.get_depth(node.right))

	def validateBST(self):
		"""
		O(N) - checks if every node has smaller-node left subtree
		 and a larger-node right subtree
		"""
		INT_MAX = 2**32
		INT_MIN = -2**32
	
		def validate(root, max, min):
			if root == None:
				return True
			if root.val > max or root.val < min:
				return False
			return validate(root.left, root.val, min) and validate(root.right, max, root.val)
		return validate(self.root, INT_MAX, INT_MIN) 
			
					
	def is_balanced(self):
		"""
		O(N) - we check every node
		Height balanced : no two subtrees of a node 
		differ in depth by more than 1
		"""
		def __is_balanced(root):
			if root == None:
				return True
			l = self.get_depth(root.left)
			r = self.get_depth(root.right)
			if abs(l-r) > 1:
				return False
			return (__is_balanced(root.left) and __is_balanced(root.right))

		return __is_balanced(self.root)
	
	def invert(self):
		"""
		O(N)
		"""
		def __invert(root):
			if root == None:
				return
			if root.left == root.right == None:
				return
			root.left, root.right = root.right, root.left
			__invert(root.left)
			__invert(root.right)
			return root
		return __invert(self.root)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(8)
bst.insert(20)
bst.insert(15)
bst.inorder()
print "postorder"
bst.postorder()
print "preorder"
bst.preorder()
print "depth:{0}".format(bst.get_depth(bst.root))
bst.delete(10)
bst.inorder()
bst.search(10)
bst.search(20)
print bst.is_balanced()
print bst.validateBST()
bst.invert()
print bst.inorder()
print bst.levelorder()
print bst.depth_first_traversal()

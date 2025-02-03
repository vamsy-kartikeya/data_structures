from collections import deque
class BinaryTree:
	def __init__(self, data):
		self.data = data  # root node
		self.left = None  # left child
		self.right = None  # right child
	# set data
	def set_data(self, data):
		self.data = data
	# get data   
	def get_data(self):
		return self.data	
	# get left child of a node
	def getLeft(self):
		return self.left
	# get right child of a node
	def getRight(self):
		return self.right
	# get left child of a node
	def setLeft(self, left):
		self.left = left
	# get right child of a node
	def setRight(self, right):
		self.right = right
	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp

def create_tree():
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    return root

def level_order_traversal(root):
	if not root:
		return []
	q = deque([root])
	levels = []
	
	while q:
		level_size = len(q)
		current_level = []
		
		for _ in range(level_size):
			node = q.popleft()
			current_level.append(node.data)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
				
		levels.append(current_level)

	# Print from bottom to up
	for level in reversed(levels):
		for val in level:
			print(val, end=" ")

def depth_of_tree(root):
	if not root:
		return 0
	q = deque([(root, 1)])
	temp = 0
	while q:
		node, dep = q.popleft()
		temp = max(temp,dep)
		if node.left:
			q.append((node.left,dep+1))
		if node.right:
			q.append((node.right,dep+1))
	print(temp)
	return temp
		
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def diameter_of_tree(root):
    if not root:
        return 0
    
    # Get heights of left and right subtrees
    lheight = height(root.left)
    rheight = height(root.right)
    
    # Get diameters of left and right subtrees
    ldiameter = diameter_of_tree(root.left)
    rdiameter = diameter_of_tree(root.right)
    
    # Return maximum of:
    # 1) Diameter through root (left height + right height)
    # 2) Diameter of left subtree
    # 3) Diameter of right subtree
    return max(lheight + rheight, max(ldiameter, rdiameter))

def width_of_tree(root):
    if not root:
        return 0
        
    q = deque([root])
    max_width = 0
    
    while q:
        level_size = len(q)
        max_width = max(max_width, level_size)
        
        for _ in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return max_width

def if_mirror(tree1, tree2):
    if (not tree1.left) and (not tree2.left) and (not tree1.right) and (not tree2.right) and tree1.data == tree2.data:
        return True
    if (tree1.data != tree2.data) or (not tree1.left and tree2.left) or (not tree2.left and tree1.left) or (not tree1.right and tree2.right) or (not tree2.right and tree2.right):
        return False
    return if_mirror(tree1.left, tree2.left) and if_mirror(tree2.right, tree2.right)

if __name__ == "__main__":
	tree = create_tree()
	tree2 = create_tree()
	level_order_traversal(tree)
	print("\nDepth:", depth_of_tree(tree))
	print("Diameter:", diameter_of_tree(tree))
	print("Width:", width_of_tree(tree))
	print(if_mirror(tree,tree2))
from collections import deque
'''Binary Tree Class and its methods'''
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


def create_complex_tree():
    """
    Creates a binary tree with 5 levels
    Tree Structure:
                                    100
                    /                                   \
                   50                                   150
            /              \                     /              \
           25               75                 125              175
        /      \         /      \           /      \         /      \
      15        35      65      85       115      135     165      185
     /  \      /  \    /  \    /  \     /  \     /  \    /  \     /  \
    8   17    31  39  60  70  80  90   110 118  131 140 160 170  180 190
   / \  / \  / \  /   /   /   \    \    \   \    \   \   \   \    \   \
  4  9 16 19 28 33 38 58  68  78   88  95  112 120 133 145 162 172 182 195
    """
    # Create root
    root = BinaryTree(100)
    
    # Level 1
    root.insertLeft(50)
    root.insertRight(150)
    
    # Level 2
    root.getLeft().insertLeft(25)
    root.getLeft().insertRight(75)
    root.getRight().insertLeft(125)
    root.getRight().insertRight(175)
    
    # Level 3
    root.getLeft().getLeft().insertLeft(15)
    root.getLeft().getLeft().insertRight(35)
    root.getLeft().getRight().insertLeft(65)
    root.getLeft().getRight().insertRight(85)
    root.getRight().getLeft().insertLeft(115)
    root.getRight().getLeft().insertRight(135)
    root.getRight().getRight().insertLeft(165)
    root.getRight().getRight().insertRight(185)
    
    # Level 4
    l4_nodes = [
        (root.getLeft().getLeft().getLeft(), 8, 17),
        (root.getLeft().getLeft().getRight(), 31, 39),
        (root.getLeft().getRight().getLeft(), 60, 70),
        (root.getLeft().getRight().getRight(), 80, 90),
        (root.getRight().getLeft().getLeft(), 110, 118),
        (root.getRight().getLeft().getRight(), 131, 140),
        (root.getRight().getRight().getLeft(), 160, 170),
        (root.getRight().getRight().getRight(), 180, 190)
    ]
    
    for node, left_val, right_val in l4_nodes:
        node.insertLeft(left_val)
        node.insertRight(right_val)
    
    # Level 5
    l5_nodes = [
        (root.getLeft().getLeft().getLeft().getLeft(), 4, 9),
        (root.getLeft().getLeft().getLeft().getRight(), 16, 19),
        (root.getLeft().getLeft().getRight().getLeft(), 28, 33),
        (root.getLeft().getLeft().getRight().getRight(), 38, None),
        (root.getLeft().getRight().getLeft().getLeft(), 58, None),
        (root.getLeft().getRight().getLeft().getRight(), 68, None),
        (root.getLeft().getRight().getRight().getLeft(), 78, None),
        (root.getLeft().getRight().getRight().getRight(), 88, 95),
        (root.getRight().getLeft().getLeft().getRight(), 112, None),
        (root.getRight().getLeft().getRight().getLeft(), 133, None),
        (root.getRight().getRight().getLeft().getLeft(), 162, None),
        (root.getRight().getRight().getRight().getLeft(), 182, None)
    ]
    
    for node, left_val, right_val in l5_nodes:
        if left_val:
            node.insertLeft(left_val)
        if right_val:
            node.insertRight(right_val)
    
    return root

def visualize_tree_pretty(root):
    """
    Prints a visual representation of the binary tree with root at top
    Args:
        root: The root node of the tree
    """
    def get_height(node):
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))
    
    def print_tree_level(node, level, space_count):
        if not node:
            return
        if level == 1:
            print(" " * space_count + str(node.data), end="")
        elif level > 1:
            print_tree_level(node.left, level - 1, space_count - 4)
            print(" " * 8, end="")
            print_tree_level(node.right, level - 1, space_count - 4)
    
    def print_connections(node, level, space_count):
        if not node or level <= 1:
            return
        if node.left:
            print(" " * (space_count - 4) + "/", end="")
        if node.right:
            print(" " * 7 + "\\", end="")
        print()
        print_connections(node.left, level - 1, space_count - 4)
        print(" " * 8, end="")
        print_connections(node.right, level - 1, space_count - 4)
    
    height = get_height(root)
    initial_space = 4 * (2 ** (height - 1))
    
    for level in range(1, height + 1):
        print_tree_level(root, level, initial_space)
        print()
        if level < height:
            print_connections(root, level, initial_space)

def visualize_tree_levels(root):
    """
    Prints a visual representation of the binary tree level by level
    Args:
        root: The root node of the tree
    """
    if not root:
        return
    
    queue = deque([(root, 0, 0)])  # (node, level, position)
    current_level = 0
    current_level_nodes = []
    
    while queue:
        node, level, pos = queue.popleft()
        
        if level > current_level:
            # Print the previous level
            print(f"Level {current_level}:", " ".join(map(str, current_level_nodes)))
            current_level = level
            current_level_nodes = []
        
        current_level_nodes.append(node.data)
        
        if node.left:
            queue.append((node.left, level + 1, pos * 2))
        if node.right:
            queue.append((node.right, level + 1, pos * 2 + 1))
    
    # Print the last level
    if current_level_nodes:
        print(f"Level {current_level}:", " ".join(map(str, current_level_nodes)))

def test_binary_tree():


    # Create a binary tree
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    
    # Create root node
    root = BinaryTree(1)
    
    # Insert left subtree
    root.insertLeft(2)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    
    # Insert right subtree
    root.insertRight(3)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    
    # Test findMax_recursive
    print("\nTesting findMax_recursive:")
    print("Expected max: 7")
    print("Actual max:", findMax_recursive(root))
    
    # Test get and set methods

    
    # Create another tree for more tests
    #     10
    #    /  \
    #   20   30
    print("\nTesting another tree:")
    tree2 = BinaryTree(10)
    tree2.insertLeft(20)
    tree2.insertRight(30)
    print("Root:", tree2.get_data())
    print("Left child:", tree2.getLeft().get_data())
    print("Right child:", tree2.getRight().get_data())

    print("\nTree Structure:")
    visualize_tree_pretty(root)

    print("\nTree Visualization (by levels):")
    visualize_tree_levels(root)




    """
    Creates a binary tree with 5 levels
    Tree Structure:
                                    100
                    /                                   \
                   50                                   150
            /              \                     /              \
           25               75                 125              175
        /      \         /      \           /      \         /      \
      15        35      65      85       115      135     165      185
     /  \      /  \    /  \    /  \     /  \     /  \    /  \     /  \
    8   17    31  39  60  70  80  90   110 118  131 140 160 170  180 190
   / \  / \  / \  /   /   /   \    \    \   \    \   \   \   \    \   \
  4  9 16 19 28 33 38 58  68  78   88  95  112 120 133 145 162 172 182 195
    """

maxData = float('-inf')
def findMax_recursive(root):
    """
    Finds the maximum value in the binary tree using recursion
    Args:
        root: Root node of the binary tree
    Returns:
        Maximum value in the tree
    """
    global maxData
    if not root:
        return maxData
    maxData = max(maxData,root.data)
    findMax_recursive(root.left)
    findMax_recursive(root.right)
    return maxData  




def find_recursive(root,data):
    """
    Searches for a value in the binary tree using recursion
    Args:
        root: Root node of the binary tree
        data: Value to search for
    Returns:
        True if value is found, False otherwise
    """
    if not root:
        return False
    if root.data == data:
        return True
    return find_recursive(root.left,data) or find_recursive(root.right,data)


def findElement_iterative(root,data):
    """
    Searches for a value in the binary tree using level-order traversal
    Args:
        root: Root node of the binary tree
        data: Value to search for
    Returns:
        True if value is found, False otherwise
    """
    if not root:
        return False
    q = deque([root])
    while q:
        node = q.popleft()
        if node.data == data:
            return True
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return False

def insert_binarytree_using_level_order(root,data):
    """
    Inserts a new value into the binary tree using level-order traversal
    Inserts at the first available position (left to right)
    Args:
        root: Root node of the binary tree
        data: Value to insert
    Returns:
        Root node of the modified tree
    """
    new_node = BinaryTree(data)
    if not root:
        root = new_node
        return root
    q = deque([root])
    while q:
        node = q.popleft()
        if data == node.get_data():
            return root
        if node.left:
            q.append(node.left)
        else:
            node.left = new_node
            return root
        if node.right:
            q.append(node.right)
        else:
            node.right = new_node
            return root


def find_size_recursion(root):
    """
    Calculates the size (number of nodes) of the binary tree using recursion
    Args:
        root: Root node of the binary tree
    Returns:
        Number of nodes in the tree
    """
    if not root:
        return 0
    return find_size_recursion(root.left) + find_size_recursion(root.right) + 1

def find_size_iterative(root):
    """
    Calculates the size (number of nodes) of the binary tree using level-order traversal
    Args:
        root: Root node of the binary tree
    Returns:
        Number of nodes in the tree
    """
    count = 0
    if not root:
        return count
    q = deque([root])
    while q:
        node = q.popleft()
        count += 1 
        if node.left: 
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return count
          
if __name__ == "__main__":
    tree = create_complex_tree()
    print("\nTree Structure:")
    # visualize_tree_pretty(tree)
    print("\nMaximum value in tree:", findMax_recursive(tree))
    print("\nIf value in tree recursive:", find_recursive(tree,190))
    print("\nIf value in tree iterative:", findElement_iterative(tree,190))
    print("\nSize of the bianry tree is :", find_size_recursion(tree))
    insert_binarytree_using_level_order(tree,10000)
    print("\nSize of the bianry tree is :", find_size_recursion(tree))
    print("\nSize of the bianry tree is in iterative :", find_size_iterative(tree))
    insert_binarytree_using_level_order(tree,10001)
    print("\nSize of the bianry tree is in interative:", find_size_iterative(tree))
    # visualize_tree_pretty(tree)

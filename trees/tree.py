class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        
        def _insert_recursive(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    _insert_recursive(node.left, value)
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    _insert_recursive(node.right, value)
        
        _insert_recursive(self.root, value)
    
    def search(self, value):
        def _search_recursive(node, value):
            if node is None or node.value == value:
                return node
            
            if value < node.value:
                return _search_recursive(node.left, value)
            return _search_recursive(node.right, value)
        
        return _search_recursive(self.root, value)
    
    def inorder_traversal(self):
        result = []
        
        def _inorder_recursive(node):
            if node:
                _inorder_recursive(node.left)
                result.append(node.value)
                _inorder_recursive(node.right)
        
        _inorder_recursive(self.root)
        return result 
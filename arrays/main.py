from binarytree import CompleteBinaryTree
import time


def main():
    # Create a complete binary tree
    tree = CompleteBinaryTree()
    
    # Values from 1 to 7
    values = list(range(1, 8))  # [1, 2, 3, 4, 5, 6, 7]
    
    # Build the tree
    tree.build_complete_tree(values)

   
    tree.preorder_traversal()
    # Final tree structure will look like:
    #       1
    #    /     \
    #   2       3
    #  / \     / \
    # 4   5   6   7

if __name__ == "__main__":
    main()

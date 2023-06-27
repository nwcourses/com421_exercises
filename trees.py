# TreeNode - represents an individual node in a tree
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def __str__(self):
        # for you to complete - return the value
        pass

    # TreeNode insert

    # is newValue less than or greater than the current value?

    # if less than, it should create a new node as the left node - but what if there is a left node already? - the recursion comes in here and we have to RECURSIVELY call insert() on the left node

    # if greater than, it should create a new node as the right node - if there is a right node already we need to RECURSIVELY call insert on the right node
    def insert(self, newValue):
        pass

################################################################################

# BinaryTree - represents the whole binary tree
class BinaryTree:
    def __init__(self):
        self.root = None

    # insert() - inserts a new value into the binary tree
    # for you to do!
    # you need to handle the possibility of there being no root

    # The BinaryTree insert() method will need to call the TreeNode insert() method
    # If there is no root node, create it
    # Otherwise, call the root node's insert() method to start the recursive process of inserting the node in the correct place
    def insert(self, value):
        
        pass
    

    # print_from()
    # print the tree, starting from a given node
    # use recursion to recursively print the left node, the value, and the right node
    def print_from(self, startNode):    
        pass

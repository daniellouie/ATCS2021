"""
Daniel Louie
ATCS 2021-2022
Binary Tree

Python program to for binary tree insertion and traversals
"""
from bst_node import Node


'''
A function that returns a string of the inorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getInorder(root):
  if (root == None):
    return ''
  return str(getInorder(root.left)) + str(root.val) + '-' + str(getInorder(root.right))


'''
A function that returns a string of the postorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
# A function to do postorder tree traversal
def getPostorder(root):
  if (root == None):
    return ''
  return str(getPostorder(root.left)) + str(getPostorder(root.right)) + str(root.val) + '-'


'''
A function that returns a string of the preorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''

def getPreorder(root):
  if (root == None):
    return ''
  return str(root.val) + '-' + str(getPreorder(root.left)) + str(getPreorder(root.right))

'''
A function that inserts a Node with the value
key in the proper position of the BST with the
provided root. The function will return the 
original root with no change if the key already
exists in the tree.
'''
def insert(root, key):
  if (root == None):
    return Node(key)
  else:
    if (root.val == root):
      return root
    elif (root.val < key):
      root.right = insert(root.right, key)
    else:
      root.left = insert(root.left, key)
    return root

'''
Challenge: A function determines if a binary tree 
is a valid binary search tree
'''
def isBST(root):
  if (root == None):
    return True
  elif (root.left != None and root.left.val > root.val):
    return False
  elif (root.right != None and root.right.val < root.val):
    return False
  elif (isBST(root.left) and isBST(root.right)):
    return True
  else:
    return False

if __name__ == '__main__':
    # Tree to help you test your code
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(9)

    print("Preorder traversal of binary tree is")
    print(getPreorder(root))

    print("\nInorder traversal of binary tree is")
    print(getInorder(root))

    print("\nPostorder traversal of binary tree is")
    print(getPostorder(root))

    root = insert(root, 8)
    print("\nInorder traversal of binary tree with 8 inserted is")
    print(getInorder(root))

    print("\nChecking if BST")
    print(isBST(root))

    

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None
    
    # Insert a node in BST
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.value:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    # In-order traversal (Left, Root, Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=' ')
            self.inorder(root.right)

    # Find minimum value node in BST
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a node from BST
    def deleteNode(self, root, key):
        if root is None:
            return root
        if key < root.value:
            root.left = self.deleteNode(root.left, key)
        elif key > root.value:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                    return root.left
            else:
                succ = self.getSucc(root.right, key)
                root.key = succ
                root.right = self.deleteNode(root.right, succ)

            return root
    
    def getSucc(curr, key):
        while curr.left != None:
            curr = curr.left

        return curr.key

# Test BST
bst = BST()
bst.root = bst.insert(bst.root, 50)
bst.insert(bst.root, 30)
bst.insert(bst.root, 20)
bst.insert(bst.root, 40)
bst.insert(bst.root, 70)
bst.insert(bst.root, 60)
bst.insert(bst.root, 80)
bst.deleteNode(bst.root,60)

print("BST In-order Traversal:")
bst.inorder(bst.root)
print("\n")

bst.root = bst.deleteNode(bst.root, 20)
print("BST In-order Traversal after deletion:")
bst.inorder(bst.root)

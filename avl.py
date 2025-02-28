class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1  # Initial height of node is 1

class AVLTree:
    def __init__(self):
        self.root = None

    # Get the height of a node
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    # Get balance factor of a node
    def getBalance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right rotate the subtree rooted at y
    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        
        return x

    # Left rotate the subtree rooted at x
    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        
        return y

    # Insert a node in AVL Tree
    def insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.value:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Update height of the ancestor node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Get the balance factor of the node
        balance = self.getBalance(node)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and key < node.left.value:
            return self.rightRotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.value:
            return self.leftRotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.value:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.value:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    # In-order traversal of the AVL tree
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=' ')
            self.inorder(root.right)

# Test AVL Tree
avl = AVLTree()
avl.root = avl.insert(avl.root, 10)
avl.root = avl.insert(avl.root, 20)
avl.root = avl.insert(avl.root, 30)
avl.root = avl.insert(avl.root, 15)
avl.root = avl.insert(avl.root, 25)

print("AVL In-order Traversal:")
avl.inorder(avl.root)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, root, key):
        if root is None or root.key == key:
            return root
        
        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                root.left.left = self.splay(root.left.left, key)
                root = self.right_rotate(root)
            elif key > root.left.key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right:
                    root.left = self.left_rotate(root.left)
            return self.right_rotate(root) if root.left else root
        
        else:
            if root.right is None:
                return root
            if key > root.right.key:
                root.right.right = self.splay(root.right.right, key)
                root = self.left_rotate(root)
            elif key < root.right.key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = self.right_rotate(root.right)
            return self.left_rotate(root) if root.right else root
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        self.root = self.splay(self.root, key)
        if self.root.key == key:
            return
        new_node = Node(key)
        if key < self.root.key:
            new_node.right, new_node.left, self.root.left = self.root, self.root.left, None
        else:
            new_node.left, new_node.right, self.root.right = self.root, self.root.right, None
        self.root = new_node
    
    def search(self, key):
        self.root = self.splay(self.root, key)
        return self.root if self.root and self.root.key == key else None
    
    def delete(self, key):
        if self.root is None:
            return
        self.root = self.splay(self.root, key)
        if self.root.key != key:
            return
        self.root = self.root.right if self.root.left is None else self.splay(self.root.left, key)
        if self.root:
            self.root.right = self.root.right
    
    def preorder(self, root):
        if root:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)

# Example usage
tree = SplayTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)

print("Preorder traversal after insertions:")
tree.preorder(tree.root)
print()

print("Searching for 30 (splayed to root):")
tree.search(30)
tree.preorder(tree.root)
print()

print("Deleting 30:")
tree.delete(30)
tree.preorder(tree.root)
print()

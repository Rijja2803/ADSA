import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(freqs):
    heap = [Node(ch, freq) for ch, freq in freqs.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left, right = heapq.heappop(heap), heapq.heappop(heap)
        new_node = Node(None, left.freq + right.freq)
        new_node.left, new_node.right = left, right
        heapq.heappush(heap, new_node)
    
    return heap[0]  # Return the root node of the tree

freqs = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
root = huffman_tree(freqs)
print(root.freq)  

import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if not data:
        return "", None

    frequency = Counter(data)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    root = heap[0]
    huffman_codes = {}

    def build_code(node, code):
        if node:
            if node.char:
                huffman_codes[node.char] = code
            build_code(node.left, code + "0")
            build_code(node.right, code + "1")

    build_code(root, "")
    encoded_data = ''.join(huffman_codes[char] for char in data)

    return encoded_data, root

def huffman_decoding(data, root):
    decoded_output = []
    current_node = root
    for bit in data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.left is None and current_node.right is None:
            decoded_output.append(current_node.char)
            current_node = root
    return ''.join(decoded_output)

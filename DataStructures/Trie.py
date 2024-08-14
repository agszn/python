class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

        def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            child_node = node.children[char]
            can_delete_child = _delete(child_node, word, index + 1)

            if can_delete_child:
                del node.children[char]
                return not node.is_end_of_word and len(node.children) == 0

            return False

        _delete(self.root, word, 0)

# Example usage
trie = Trie()
trie.insert("hello")
print(trie.search("hello"))  # True
trie.delete("hello")
print(trie.search("hello"))  # False

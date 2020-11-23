class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


"""
Trie that returns the first 3 suggestions for a given query 
"""


class Trie(object):
    output = []

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True

    def dfs(self, node, prefix):
        if len(self.output) >= 3:
            return

        if node.is_end:
            self.output.append(prefix + node.char)

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, query):
        self.output = []
        node = self.root

        for char in query:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, query[:-1])

        return self.output


class Suggester:
    prods = []
    trie = Trie()

    def __init__(self):
        f = open("words.txt", "r")
        for word in f.read().split("\n"):
            self.trie.insert(word)
        f.close()

    def suggest(self, test_case):
        return self.trie.query(test_case)

    def test(self):
        for test_case in ["Sta", "Rec", "Pick"]:
            ans = self.suggest(test_case)
            print(f"For '{test_case}' suggestions are: {ans}")


suggester = Suggester()
suggester.test()

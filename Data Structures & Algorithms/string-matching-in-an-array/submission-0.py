class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_suffix(self, word):
        for i in range(len(word)):
            node = self.root
            for j in range(i, len(word)):
                idx = ord(word[j]) - 97
                if not node.children[idx]:
                    node.children[idx] = TrieNode()

                node = node.children[idx]
                node.count += 1

    def search(self, word):
        node = self.root
        for char in word:
            idx = ord(char) - 97
            node = node.children[idx]
        return node.count > 1



class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        ans = []
        t = Trie()

        for w in words:
            t.insert_suffix(w)

        for w in words:
            if t.search(w):
                ans.append(w)


        return ans
        
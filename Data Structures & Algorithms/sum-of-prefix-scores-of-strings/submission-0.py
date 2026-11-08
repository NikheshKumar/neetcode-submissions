class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        # trie building
        root = TrieNode()

        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1
                

        # word scoring
        ans = []
        for w in words:
            node = root
            total = 0
            for char in w:
                node = node.children[char]
                total += node.count
            ans.append(total)

        return ans


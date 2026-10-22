class TrieNode:

    def __init__(self):
        self.word = False
        self.children = {}

    def AddWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for w in words:
            root.AddWord(w)

        m, n = len(board), len(board[0])

        res = set()
        visited = set()

        def dfs(r,c,node, word):

            invalid = (r<0) or (c<0) or (r>=m) or (c>=n) or (board[r][c] not in node.children) or ((r,c) in visited)

            if invalid:
                return False

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.word:
                node.word = False
                res.add(word)

            dfs(r+1,c,node,word) 
            dfs(r-1,c,node,word)
            dfs(r,c+1, node, word)
            dfs(r,c-1, node,word)
            
            visited.remove((r,c))

        for r in range(m):
            for c in range(n):
                dfs(r,c,root, "")

        
        return list(res)




            
        


        
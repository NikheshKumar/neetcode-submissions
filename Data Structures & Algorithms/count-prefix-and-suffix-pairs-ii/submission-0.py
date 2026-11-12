class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        edges = {}
        ends = [0]
        ans = 0

        for w in words:
            node = 0
            for i, char in enumerate(w):
                n = len(w)
                key = node * 676 + (ord(char)-97)*26 + (ord(w[n-1-i])) - 97
                if key not in edges:
                    edges[key] = len(ends)
                    ends.append(0)

                node = edges[key]
                ans += ends[node]

            ends[node] += 1


        return ans



        

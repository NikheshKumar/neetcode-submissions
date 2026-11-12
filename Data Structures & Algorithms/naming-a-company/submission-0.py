class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        groups = [set() for _ in range(26)]

        for w in ideas:
            groups[ord(w[0])-ord('a')].add(w[1:])

        ans = 0

        for i in range(26):
            for j in range(i+1, 26):
                common = len(groups[i] & groups[j])
                ans += 2*(len(groups[i]) - common)*(len(groups[j]) - common)

        return ans
        

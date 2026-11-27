class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False

        m1, m2 = {}, {}

        for char, word in zip(pattern, s):
            if char in m1 and m1[char]!=word:
                return False
            if word in m2 and m2[word]!=char:
                return False
            m1[char] = word
            m2[word] = char


        return True
        
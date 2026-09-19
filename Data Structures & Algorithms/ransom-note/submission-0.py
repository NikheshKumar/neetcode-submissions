class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)

        for char in ransomNote:
            if m[char]==0:
                return False
            m[char] -= 1

        return True


        
        
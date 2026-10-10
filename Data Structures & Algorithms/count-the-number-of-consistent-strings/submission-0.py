class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = len(words)

        chars = set(allowed)

        for w in words:
            for c in w:
                if c not in chars:
                    count -= 1
                    break

        return count
        
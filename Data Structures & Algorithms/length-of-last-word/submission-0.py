class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        r = len(s)-1
        ans = 0

        while r>=0 and s[r] == " ":
            r -= 1
  
        while r>=0 and s[r] != " ":
            r -= 1
            ans += 1

        return ans


            


        
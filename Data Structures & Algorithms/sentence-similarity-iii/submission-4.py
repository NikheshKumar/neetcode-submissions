class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        l = 0
        while l<len(s1) and s1[l]==s2[l]:
            l+=1

        r = 0
        while r<len(s1)-l and s1[-r-1]==s2[-r-1]:
            r+=1

        return l+r == len(s1)

        

        

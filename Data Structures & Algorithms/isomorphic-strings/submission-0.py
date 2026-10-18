class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        m1, m2 = {}, {}
        for c1, c2 in zip(s,t):
            if m1.get(c1,c2)!=c2 or m2.get(c2,c1)!=c1:
                return False

            m1[c1] = c2
            m2[c2] = c1

        return True

        
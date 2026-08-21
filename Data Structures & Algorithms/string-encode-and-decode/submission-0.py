class Solution:

    def encode(self, strs: List[str]) -> str:

        enc_string = []
        for s in strs:
            t = str(len(s)) + "#" + s
            enc_string.append(t)
        return "".join(enc_string)

    def decode(self, s: str) -> List[str]:

        i = 0
        dec_string = []

        while i < len(s):
            j = i
            l = 0
            while s[j]!="#":
                j += 1
            l = int(s[i:j])
            dec = s[j+1:j+1+l]
            dec_string.append(dec)
            i = j + 1 + l

        return dec_string

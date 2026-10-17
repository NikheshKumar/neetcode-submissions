class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        ans = [i for i in code]
        n = len(code)

        for i in range(n):
            total = 0

            for j in range(1,abs(k)+1):
                idx = (j+i)%n if k>0 else (i-j)%n
                total += code[idx]

            ans[i] = total

        
        return ans


        

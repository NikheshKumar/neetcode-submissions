class Solution:
    def mySqrt(self, x: int) -> int:

        if x==0:
            return 0

        low = 0
        high = x

        ans = 0
    
        while low<=high:
            mid = (low+high)//2
            if (mid**2)<=x:
                ans = mid
                low = mid + 1
            if (mid**2) > x:
                high = mid - 1

        return ans


            

            
        
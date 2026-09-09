class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r = len(arr) - 1
        greatest = -1
        
        while r >= 0:
            temp = arr[r]
            arr[r] = greatest
            greatest = max(temp, greatest)
            r -= 1

        return arr
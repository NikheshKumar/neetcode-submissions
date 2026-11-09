class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        s = set(folder)

        ans = []

        for f in folder:
            address = f.split("/")
            sub = False
            for i in range(1,len(address)-1):
                if "/".join(address[:i+1]) in s:
                    sub = True
                    break
            if sub==False:
                ans.append(f)

        return ans


        
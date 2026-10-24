class FreqStack:

    def __init__(self):
        self.levels = [[]]
        self.count = defaultdict(int)
        

    def push(self, val: int) -> None:
        self.count[val]+=1
        f = self.count[val]
        if f==len(self.levels):
            self.levels.append([])
        self.levels[f].append(val)
        

    def pop(self) -> int:
        v = self.levels[-1].pop()
        self.count[v] -= 1
        if not self.levels[-1]:
            self.levels.pop()
        return v
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
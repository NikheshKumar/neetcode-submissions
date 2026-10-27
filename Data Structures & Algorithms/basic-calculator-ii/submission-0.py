class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        op = '+'
        n = len(s)
        s = s + "+"

        for i,ch in enumerate(s):
            if ch==' ':
                continue
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            else:
                if op=='+':
                    stack.append(curr)
                elif op=="-":
                    stack.append(-curr)
                elif op=="*":
                    stack.append(stack.pop()*curr)
                else:
                    top = stack.pop()
                    stack.append(-(-top // curr) if top < 0 else top // curr)

                op = ch
                curr = 0

        


        return sum(stack)
            
                

        
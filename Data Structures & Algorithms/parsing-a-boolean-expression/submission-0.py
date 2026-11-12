class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            if char==",":
                continue
            if char!=")":
                stack.append(char)
                continue
            yes = no = False
            while stack[-1] != "(":
                val = stack.pop()
                yes |= val=="t"
                no |= val=="f"
            stack.pop()
            op = stack.pop()
            val = False
            if op == "!":
                val = not yes
            else:
                val = (not no) if op=="&" else yes

            stack.append("t" if val else "f")

        return stack[0]=="t"

            
        

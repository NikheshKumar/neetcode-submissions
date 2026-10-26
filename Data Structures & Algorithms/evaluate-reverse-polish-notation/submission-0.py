class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in {"+", "-", "*", "/"}:
                curr1 = stack.pop()
                curr2 = stack.pop()
                if char=="-":
                    stack.append(curr2 - curr1)
                elif char=="/":
                    stack.append(int(curr2/curr1))
                elif char=="+":
                    stack.append(curr2+curr1)
                else:
                    stack.append(int(curr2)*int(curr1))

            else:
                stack.append(int(char))

        return stack[0]
        
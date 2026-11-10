class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def parsing(formula,i):
            if i>= len(formula) or (not formula[i].isdigit()):
                return 1,i
            j = i

            while j < len(formula) and formula[j].isdigit():
                j += 1
            return int(formula[i:j]), j

        i = 0
        stack = [{}]

        while i < len(formula):
            char = formula[i]

            if char == "(":
                stack.append({})
                i += 1

            elif char == ")":
                i += 1
                n,i = parsing(formula,i)
                top = stack.pop()
                for k in top:
                    top[k] *= n
                for k,v in top.items():
                    stack[-1][k] = stack[-1].get(k,0) + v

            elif char.isupper():
                j = i+1
                while j<len(formula) and formula[j].islower():
                    j += 1
                element = formula[i:j]
                n,i = parsing(formula,j)
                stack[-1][element] = stack[-1].get(element,0) + n



        res = stack[0]
        return "".join(
    ele + (str(res[ele]) if res[ele] > 1 else "") for ele in sorted(res)
)



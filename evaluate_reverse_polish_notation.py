# time: O(n)
# space: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t != "+" and t != "-" and t != "*" and t != "/":
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if t == "+":
                    stack.append(op1 + op2)
                elif t == "-":
                    stack.append(op1 - op2)
                elif t == "*":
                    stack.append(op1 * op2)
                elif t == "/":
                    # do not use integer division //: for negative numbers it will round away from 0
                    stack.append(trunc(op1 / op2))
                #print(f"{op1} {t} {op2} = {stack[-1]}")

        return stack.pop()

# time = O(n)
# space = O(n)

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        op = "+"
        stack = []
        
        for i, c in enumerate(s):
            # extract number
            if c in "0123456789":
                num = num * 10 + int(c)
            # take action on operator or end of string
            if c in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                # precedence implementation for / and *:
                # operate on top of stack
                elif op == '*':
                    val = stack.pop() * num
                    stack.append(val)
                elif op == '/':
                    val = int(stack.pop() / num)
                    stack.append(val)
            
                op = c
                num = 0
       
        return sum(stack)

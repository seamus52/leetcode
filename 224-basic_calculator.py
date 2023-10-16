# time: O(n)
# space: O(1)
# time: O(n)
# space: O(1)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        acc = 0
        sign = 1

        for c in s:
            if c.isdigit():
                # Forming operand, since it could be more than one digit
                num = (num * 10) + int(c)
            elif c == '+':
                acc += sign * num
                # Save the recently encountered '+' sign
                sign = 1
                num = 0
            elif c == '-':
                acc += sign * num
                sign = -1
                num = 0
            elif c == '(':
                # Push the result and sign on to the stack, order matters
                stack.append(acc)
                stack.append(sign)
                # Reset operand and result, new evaluation begins for the new sub-expression
                sign = 1
                acc = 0
            elif c == ')':
                # Evaluate the expression to the left with result, sign and operand
                acc += sign * num
                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                acc *= stack.pop() # stack pop 1, sign
                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                acc += stack.pop() # stack pop 2, operand
                # Reset the operand
                num = 0

        return acc + (sign * num)

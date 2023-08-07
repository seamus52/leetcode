# stack - handle nesting -> put back to stack
# time: O(approx k^k*n)
# space: O(approx k^k*n)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [];
        curNum = 0;
        curString = ""
        
        for c in s:
            if c == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif c == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                # keep track of multi-digit numbers
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        
        return curString


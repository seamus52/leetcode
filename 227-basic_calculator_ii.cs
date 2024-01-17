public class Solution {
    public int Calculate(string s) {
        Stack<int> stack = new();
        int num = 0;
        char op = '+';

        for (int i = 0; i < s.Length; i++)
        {
            if (Char.IsDigit(s[i]))
            {
                num = num * 10 + Convert.ToInt32(Char.GetNumericValue(s[i]));
            }
            if ("+-*/".Contains(s[i]) || i == s.Length - 1)
            {
                if (op == '+')
                {
                    stack.Push(num);
                }
                else if (op == '-')
                {
                    stack.Push(-num);
                }
                else if (op == '*')
                {
                    stack.Push(stack.Pop() * num);
                }
                else if (op == '/')
                {
                    stack.Push(stack.Pop() / num);
                }

                num = 0;
                op = s[i];
            }

        }

        return stack.ToArray().Sum();
    }
}

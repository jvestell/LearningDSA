"""
Given a string s of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
        return len(stack)

solution = Solution()
print(solution.minAddToMakeValid("())"))
print(solution.minAddToMakeValid("((("))

"""
Solved on: 10/19/2024
"""

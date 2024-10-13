"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets are closed by the same type of brackets.
Open brackets are closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (top, char) not in [("(", ")"), ("{", "}"), ("[", "]")]:
                    return False
        return not stack

        

solution = Solution()
print(solution.isValid("()"))

print(solution.isValid("()[]{}"))

print(solution.isValid("(]"))
        

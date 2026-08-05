class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
                        "[": "]",
                        "(": ")",
                        "{": "}"}
        stack = []
        for char in s:
            if char in open_to_close:
                stack.append(char)
            else:
                if stack and char == open_to_close[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
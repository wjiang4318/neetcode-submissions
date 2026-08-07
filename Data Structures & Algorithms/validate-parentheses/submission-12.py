class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {"}": "{",
                        ")": "(",
                        "]": "["}
        stack_list = []

        for char in s:
            if char not in close_to_open:
                stack_list.append(char)
            else: # what if it a closing bracket ]
                if stack_list and stack_list[-1] == close_to_open[char]:
                    stack_list.pop()
                else:
                    return False
        return False if stack_list else True
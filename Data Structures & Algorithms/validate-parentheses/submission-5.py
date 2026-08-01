class Solution:
    def isValid(self, input: str) -> bool:
        while "[]" in input or "{}" in input or "()" in input:
            input = input.replace("[]", '')
            #print(input)
            input = input.replace("{}", '')
            #print(input)
            input = input.replace("()", '')
            #print(input)
        return input == ""
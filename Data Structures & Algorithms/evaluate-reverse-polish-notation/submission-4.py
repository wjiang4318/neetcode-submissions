class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']: # numbers
                stack.append(int(token))
            else: #token
                a = stack.pop() # most recent number
                b = stack.pop() # second to last number
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(b-a)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    stack.append(int(b/a))
        return stack[0]


# After each operation, push the result back to the stack.
# operators follows the operands
# to add numbers it looks like 1 2 + instead of 1 + 2
# 3-4 + 5 will be 3 4 - 5 +
# ["1", "2", "3", "+", "4", "*", "+"] (which is 1 + (2+3)*4 = 21)
#["4","13","5","/","+"]
# ((13/5)+4)=6.6
# To solve this:
# value = 0 --> this value will get updated across operations
# create a list adding elements:
    # if token is a number:
        # append to list
    # else: --> token is an operands
        # if list is not empty we take all value in list and do operations
        # using the first element as the start (ie:1) + (2)
        # update value
        # then pop how many elements there are
'''
loop 1:
list = [1]

loop 2:
list = [1 ,2]

loop 3:
+

'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []

        for i in range(len(temperatures)):
            if not stack: #if stack is empty, at the start, append first element
                stack.append(i)
                #print(stack)
            else: # while stack is not empty and new temp is higher
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    popped_index = stack.pop()
                    output[popped_index] = i - popped_index
                else:  # while stack is not empty and new temp is lower than stack 
                    stack.append(i)  
        return output
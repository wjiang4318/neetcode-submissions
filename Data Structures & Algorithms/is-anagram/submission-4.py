class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        S_dict = {}
        T_dict = {}
        for char in s:
            S_dict[char] = S_dict.get(char, 0) + 1
        for char in t:
            if char in T_dict:
                T_dict[char] = T_dict[char] + 1
            else:
                T_dict[char] = 1
        return True if S_dict == T_dict else False
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty_dict = {}
        empty_list = []
        for string in strs:
            key = ''.join(sorted(string)) #act, #pots --> opst
            if key not in empty_dict: # evaulate if sort anagram exist, if not create a key with empty list
                empty_dict[key] = []
            empty_dict[key].append(string) # if sort anagram exist, we add the string to it

        return list(empty_dict.values())
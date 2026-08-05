class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            # print("".join(sorted(word)))
            key = "".join(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        return list(hashmap.values())
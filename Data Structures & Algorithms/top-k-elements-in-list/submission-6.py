class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}

        for number in nums:
            if number not in hash_table:
                hash_table[number] = 0
            hash_table[number] += 1

        sorted_hash = dict(sorted(hash_table.items(), key = lambda item: item[1], reverse= True))
        list_table = list(sorted_hash.items())[:k]
        new_list = [element[0] for element in list_table]
        return sorted(new_list)
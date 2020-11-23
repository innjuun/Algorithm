# brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# two-pass hash table
class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, nums, target):
        hash_table = {}
        ans = []
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for index, value in enumerate(nums):
            result = target - value
            hash_index = hash_table.get(result)
            if hash_index and hash_index != index:
                return [index, hash_index]


# one-pass hash table
class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, nums, target):
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict.keys():
                return [i, buff_dict[nums[i]]]
            else:
                buff_dict[target - nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = list()
            dic[nums[i]].append(i)
            
        for key, value in dic.items():
            remain_num = target - key
            if remain_num in dic:
                for kv in dic[remain_num]:
                    
                    if kv != value[0]:
                        return [value[0], kv]
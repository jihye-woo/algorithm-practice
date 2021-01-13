class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice =  [i for i in range(len(nums))]
        for pair in combinations(indice, 2):
            if nums[pair[0]] + nums[pair[1]] == target:
                return pair
        return [0, 0]
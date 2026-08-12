class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            searched = target - value

            if searched in seen:
                return [seen[searched], index]

            seen[value] = index
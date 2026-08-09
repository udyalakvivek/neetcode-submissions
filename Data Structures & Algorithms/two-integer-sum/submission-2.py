class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        deference = 0
        for i in range(0,len(nums)):
            deference = target-nums[i]
            print("deference", deference)
            if deference in seen:
                return [seen[deference], i]
            else:
                seen[nums[i]] = i
        return []

        
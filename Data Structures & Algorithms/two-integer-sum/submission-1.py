class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                total = nums[i]+nums[j]
                if total == target:
                    return [i,j]
                j += 1
            i +=1
        return []

        
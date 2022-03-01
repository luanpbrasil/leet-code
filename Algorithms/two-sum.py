class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            base_value = nums[i]
            for j in range(i+1, len(nums)):
                two_sum = base_value + nums[j]
                if two_sum == target:
                    return [i, j]
        return []
        
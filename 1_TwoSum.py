class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            another_answer = target - nums[i]
            if(another_answer in nums[i+1:]):
                answer = [i, nums[i+1:].index(another_answer)+i+1]
        return answer
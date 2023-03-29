class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            for ii in range(i+1, len(nums)):
                if nums[i] + nums[ii] == target:
                    answer.append(i)
                    answer.append(ii)
                    return answer

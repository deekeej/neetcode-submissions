class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNumber=0
        counter = 0
        for z in range(len(nums)):
            if nums[z] == 0:
                maxNumber=max(maxNumber, counter)
                counter=0
            else:
                counter+=1
        return max(maxNumber, counter)
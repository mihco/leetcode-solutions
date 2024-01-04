class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsPair = []
        for i in range(len(nums)):
            numsPair.append([nums[i], i])
        numsPair.sort()
        frontInd = 0
        endInd = len(numsPair) - 1
        for i in range(len(numsPair)):
            if(numsPair[frontInd][0] + numsPair[endInd][0] == target):
                break
            elif(numsPair[frontInd][0] + numsPair[endInd][0] < target):
                frontInd += 1
            else:
                endInd -= 1
        return [numsPair[frontInd][1], numsPair[endInd][1]]
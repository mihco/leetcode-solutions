class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1
        curr_target = ""
        while(curr_target != target):
            curr_target = numbers[front] + numbers[back]
            if(curr_target == target):
                return [front + 1, back + 1]
            elif(curr_target < target):
                front += 1
            else:
                back -= 1
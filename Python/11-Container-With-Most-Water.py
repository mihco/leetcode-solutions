class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        back = len(height) - 1
        max_area = 0
        while(front < back):
            curr_area = 0
            if(height[front] > height[back]):
                curr_area = height[back] * (back - front)
                back -= 1
            else:
                curr_area = height[front] * (back - front)
                front += 1
            if curr_area > max_area:
                max_area = curr_area
            
        return max_area
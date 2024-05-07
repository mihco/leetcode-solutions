class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_height = 0
        
        for i in range(len(heights)):
            if(i == 0):
                stack.append([heights[i], i])
                max_height = heights[i] * (i + 1)
                continue
            if(len(stack) == 0 or heights[i] >= stack[-1][0]):
                stack.append([heights[i],i])
            else:
                while(len(stack) != 0 and heights[i] < stack[-1][0]):
                    top = stack.pop()
                    top_height = top[0] * (i - top[1])
                    if(top_height > max_height):
                        max_height = top_height
                stack.append([heights[i], top[1]])
        
        for i in range(len(stack)):
            top_height = stack[i][0] * (len(heights) - stack[i][1])
            if(top_height > max_height):
                max_height = top_height
        
        return max_height
            
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # potato s(t)ack :)
        path = []
        for i in range(len(position)):
            path.append([position[i],speed[i]])
        path.sort()
        for i in range(len(path) - 1, -1, -1):
            stack.append(path[i])
            if(len(stack) > 1 and (target - stack[-1][0]) / stack[-1][1] <= (target - stack[-2][0]) / stack[-2][1]):
                stack.pop()
        
        return len(stack)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = tuple(temperatures)
        answer = [0] * len(temps)
        stack = []
        for i in range(len(temps)):
            stack.append((temps[i], i))
            if(i == len(temps) - 1):
                answer[-1] = 0
                break;
            while(len(stack) > 0 and stack[-1][0] < temps[i+1]):
                answer[stack[-1][1]] = i+1-stack[-1][1]
                stack.pop()
        return answer
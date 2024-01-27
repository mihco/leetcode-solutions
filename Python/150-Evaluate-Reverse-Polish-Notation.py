class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            try:
                int(t)
                stack.append(int(t))
            except ValueError:
                first = stack.pop()
                second = stack.pop()
                if(t == "+"):
                    stack.append(first + second)
                elif(t == "-"):
                    stack.append(second - first)
                elif(t == "*"):
                    stack.append(first * second)
                else:
                    stack.append(int(second / first))
        return stack[0]
                
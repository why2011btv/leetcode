from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                number2 = stack.pop()
                number1 = stack.pop()
                if token == '+':
                    stack.append(number1 + number2)
                elif token == '-':
                    stack.append(number1 - number2)
                elif token == '*':
                    stack.append(number1 * number2)
                else:
                    stack.append(int(number1 / number2))
            else:
                stack.append(int(token))
        #assert len(stack) == 1
        return stack.pop()


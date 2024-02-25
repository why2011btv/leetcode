class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current, open, close, n):
            if open > n or close > n or open < close:
                return
            elif len(current) == 2*n:
                output.append(current)
                return 

            for next_p in ['(', ')']:
                if next_p == '(':
                    backtrack(current + next_p, open+1, close, n)
                else:
                    backtrack(current + next_p, open, close+1, n)
        
        output = []
        backtrack('(', 1, 0, n)
        return output

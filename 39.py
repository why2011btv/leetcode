def combinationSum(candidates, target):
    def backtrack(remain, combo, start):
        if remain == 0:
            # Make a deep copy of the current combination,
            # otherwise it will be affected by the subsequent modifications.
            result.append(list(combo))
            return
        elif remain < 0:
            # Exceed the scope, stop exploration.
            return
        
        for i in range(start, len(candidates)):
            # Add the number into the combination
            combo.append(candidates[i])
            # Give the current number another chance, since it can be used unlimited times.
            backtrack(remain - candidates[i], combo, i)
            # Backtrack, remove the number from the combination
            combo.pop()
    
    result = []
    backtrack(target, [], 0)
    return result

# Example usage
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))

# https://chat.openai.com/share/5fecaf38-26b3-477c-b09b-94bb078b56f7

# Things learned from this:
# 1) function calling order in backtracking
# 2) difference between result.append(list(combo)) & result.append(combo)
# 3) combo.pop() pops out the last added element

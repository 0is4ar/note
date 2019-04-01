# letter combinations of a phone number


## mine 

```python
class Solution:
    def __init__(self):
        self.map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
    def letterCombinations(self, digits):
        if digits == '':
            return []
        if len(digits) == 1:
            return [i for i in self.map[digits]]
        pool = []
        for i in digits:
            pool.append(self.map[i])
        from functools import reduce    
        result = reduce(self.product, pool)    
        return result
        
    def product(self,a,b):
	''' 
	product("abc","abc") -> ["aa","ab","ac","ba",'bb","bc","ca","cb","cc"]
	product(["ab","ac"],"d") -> ['abd','acd']
	'''
        res_list = []
        for i in a:
            for j in b:
                ele = i+j
                res_list.append(ele)
        return res_list
```

## Solution

```python
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output<Paste>
```

- time complexity: O(3^N * 4^M).
N is the number of digits that have three key. Same for M.

- space: O(3^N * 4^M) 
there's (3^N * 4^N) solutions, every may take constant c space.

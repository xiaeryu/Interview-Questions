##########################################################
## Input : a string
## Output: length of the longest palindrome within the string
##########################################################

class Solution:
    # @param s, a string
    # @return an integer
    def partition(self, s):
        total = len(s)
        if total <= 1:
            return total

        rev = s[::-1]
        storage = [[0 for i in range(total)] for j in range(total)]
        for i in range(total):
            for j in range(total):
                if s[i] == rev[j]:
                    if i==0 or j == 0:
                        storage[i][j] = 1
                    else:
                        storage[i][j] = storage[i-1][j-1] +1

        return max(map(max,storage))

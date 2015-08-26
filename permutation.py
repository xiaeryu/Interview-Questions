# Find all permutations of a string.

class Solution:
    def __init__ (self, inStr):
        self.inStr = inStr
        self.mark = [0 for i in xrange(len(inStr))]
    tmpStr = ""
    output = set()
    
    def permutation(self, pos):
        if pos == len(self.inStr):
            if self.tmpStr not in self.output:
                self.output.add(self.tmpStr)
               
        for i in range(len(self.inStr)):
            if self.mark[i] == 0:
                self.tmpStr += self.inStr[i]
                self.mark[i] = 1
                self.permutation(pos+1)
                self.mark[i] = 0
                self.tmpStr = self.tmpStr[:-1]

        return self.output

t = Solution("abbc")
print t.permutation(0)

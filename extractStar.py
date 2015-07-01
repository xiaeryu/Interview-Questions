## 函数将字符串中的字符“*”移到字符转的前部分，非“*”的部分后移，但不改变其内部的先后顺序，返回字符串中“*“的个数。

class Solution:
    def procString(self,instr):
        total = len(instr)
        if total == 0:
            return 0
        outstr = instr.replace('*','')
        target = total - len(tmpstr)
        outstr = '*' * target + outstr
        print outstr
        return target

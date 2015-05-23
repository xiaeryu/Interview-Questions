import sys

nargs = len(sys.argv)
if nargs < 3:
    print "Usage:" + sys.argv[0] + " <total number in a circle><the number that is to be deleted>"
    sys.exit()

total = sys.argv[1]
target = sys.argv[2]
total = int(total)
target = int(target)

store = [1 for i in range(0,total)]

count = 0
start = 0
while sum(store) > 1:
    count += store[start]
    if count == target:
        store[start] = 0
        count = 0
        print str(start) + "removed at this stage"

    if start < (total-1):
        start += 1
    else:
        start = 0

print store.index(1)

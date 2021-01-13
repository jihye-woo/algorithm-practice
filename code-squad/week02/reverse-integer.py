import sys

x = '-2147483648'
max_val, min_val = str(2**31 - 1), str(-2**31)
target = ''
signed = False
for w in reversed(str(x)):
    if w == '-':
        signed = True
        continue
    target += w
target = str(int(target))
if signed:
    target = '-' + target
    if(len(min_val) < len(target)): print(0)
    if (len(min_val) == len(target) and min_val < target): print(0)

else:
    if(len(max_val) < len(target)): print(0)
    if (len(max_val) == len(target) and target > max_val): print(0)

print(target)

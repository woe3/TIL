import sys
n = int(sys.stdin.readline())

fn1 = 1
fn2 = 1

for i in range(n-1):
    temp = fn1 % 15746
    fn1 = fn2 % 15746
    fn2 = fn2 + temp
    
print(fn2 % 15746)
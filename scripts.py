def superDigitRec(n):
    
    if len(n)>1:
        new_number = 0 
        for i in range(len(n)):
            new_number += int(n[i])
       
        return superDigitRec(str(new_number))
    return int(n)


def superDigit(n, k):
    initial_sum = 0
    for digit in n:
        initial_sum += int(digit)
    total = initial_sum * k
    return superDigitRec(str(total))


##########################################
# Number line jumps

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    if (x2>x1 and v2>v1) or (x1>x2 and v1>v2):
        return "NO"
    if v2==v1 and x2!=x1:
        return "NO"
        
    gap = x2 - x1
    speed_diff = v1 - v2
    
    if gap % speed_diff == 0:
        return "YES"
    else:
        return "NO"
####################################
#  XML2 - Find the Maximum Depth



maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    
    level = level + 1

    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)



####################################
#  Birthday Cake Candles

def birthdayCakeCandles(candles):
    max_size = candles[0]
    num_tallest = 0
    
    for candle_size in candles:
        if candle_size>max_size:
            num_tallest, max_size = 1, candle_size
        elif candle_size == max_size:
            num_tallest += 1
    
    return num_tallest

####################################
#  Collections.OrderedDict()

from collections import OrderedDict

n = int(input())
shop_list = OrderedDict()

for _ in range(n):
    line = input().split()
    net_price = int(line[-1])
    name = " ".join(line[:-1])
    
    if name in shop_list:
        shop_list[name] += net_price
    else:
        shop_list[name] = net_price
    
for name, price in shop_list.items():
    print(name, price)


####################################
#  Collections deque
from collections import deque

d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)

print(*d)



####################################
#  Word order


from collections import defaultdict
words = defaultdict()

n = int(input())
for _ in range(n):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words.items()))
for _,count in words.items():
    print(count, end=" ")



####################################
#  Tiem delta

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_date = "%a %d %b %Y %H:%M:%S %z"
    t1_formatted = dt.datetime.strptime(t1,format_date)
    t2_formatted = dt.datetime.strptime(t2,format_date)
    diff_seconds = abs(int((t1_formatted - t2_formatted).total_seconds()))
    
    return f"{diff_seconds}"



####################################
#  Default dict tutorial
from collections import defaultdict
n, m = map(int, input().split())

positions = defaultdict(list)
words= []
for idx in range(1, n + 1):
    word = input().strip()
    positions[word].append(str(idx))
    
for idx in range(1, m + 1):
    target = input()
    if target in positions:
        print(" ".join(positions[target]))
    else:
        print("-1")
    

# I couldnt fit every because apparentlty they weren't saved in hackerrank - 
# At least when I cliked in submissions
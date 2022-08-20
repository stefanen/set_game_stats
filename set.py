import random
import itertools
import collections
def ternary (n):
    if n == 0:
        return '0000'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return (''.join(reversed(nums))).rjust(4,'0')

def is_set(x,y,z):
    for i in range(4):
        if ((int(x[i])+int(y[i])+int(z[i]))%3!=0):
            return False
    return True

all_cards=[]
for i in range(81):
	all_cards.append(ternary(i))

print(f'all_cards={all_cards}')
example_board=random.sample(all_cards,12)
print(f'example_board with 12 cards={example_board} has possible sets:')
for c in itertools.combinations(example_board,3):
    if (is_set(c[0],c[1],c[2])):
        print(c)

stats=[]
for i in range(100000):
    set_count=0
    board=random.sample(all_cards,12)
    for c in itertools.combinations(board,3):
        if (is_set(c[0],c[1],c[2])):
            set_count+=1
    stats.append(set_count)
stats=collections.Counter(stats)
for i in stats.most_common():
    print(f'A random board contains {i[0]} possible sets with probability {i[1]/1000} %')

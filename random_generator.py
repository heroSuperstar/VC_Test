import random

num = round(random.uniform(0,100),1)
other_num = round(random.uniform(0,100),1)
diff = round(num - other_num,1)

while num > other_num:
    print('calculating')


print(f'Your random percentage is {num}%, '
          f'which is {diff}% different to {other_num}%')

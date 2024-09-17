import random

num = round(float(input('Please input a number between 1 and 100')),1)
other_num = round(random.uniform(0,100),1)
diff = round(num - other_num,1)
ackno = False



# Print numbers
print(f'Your random percentage is {num}%, '
          f'which is {diff}% different to {other_num}%')


while ackno == False:
    ans = bool(input('Accept that i am right:'))

    if ans != True:
        print('You have not accepted i am right.')
    
    else:
        print('Good, now go and tell people i am right!')
        ackno = ans







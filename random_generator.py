import random

num = round(float(input('Please input a number between 1 and 100')),1)
other_num = round(random.uniform(0,100),1)
diff = round(num - other_num,1)
ackno = False



# Print numbers
print(f'Your random percentage is {num}%, '
          f'which is {diff}% different to {other_num}%')


while ackno == False:
    ans = bool(input('Accept the Truth:'))

    if ans != True:
        print('You have not accepted the truth.')
    
    else:
        print('Good, now go and defy your fate!')
        ackno = ans







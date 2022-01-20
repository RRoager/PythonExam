import math as m
import random as r

inp = input('Get a random number between 0 and: ')
random_no = r.randint(0, int(inp))
square_root = m.sqrt(random_no)
print(f'This is your random number: {random_no}')
print(f'The square root of {random_no} is {square_root}')

choices = list(range(r.randint(0, int(inp))))
r.shuffle(choices)
print(choices.pop())
while choices:
    if input('Want another random number?(Y/N)' ).lower() == 'n':
        break
    print(choices.pop())





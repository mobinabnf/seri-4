from random import randint

choices= {1:'rock', 2:'paper', 3:'scissors'}
cpu = choices[randint(1,3)]
user = choices[int(input('Input your choice from 1 to 3:\n1: Rock, 2: Paper, 3: Scisors\n'))]
if cpu == user:
    print('\nI had the same choice! No winner.')
elif 'rock' and 'scissors' in cpu + user:
    if min(cpu,user) == cpu:
        print(f'\nMy choice was {cpu}, you chose - {user} -. I won!')
    else:
        print(f'\nMy choice was {cpu}, you chose - {user} -. You won!')
else:
    if max(cpu,user) == cpu:
        print(f'\nMy choice was - {cpu} -, you chose - {user} -. I won!')
    else:
        print(f'\nMy choice was {cpu}, you chose - {user} -. You won!')

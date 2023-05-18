import random
paper = """
       _  / |
      / \ | | /\\
       \ \| |/ /
        \ Y | /___
      .-.) '. `__/
     (.-.   / /
         | ' |
         |___|
        [_____]
        |     |
"""
scissors =""""
     (\ ||
      \\||
     /\(\L
     \/ > )
      \( (
       \  \
"""
rock = """
    ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""
yours = input("Choose: ")
choose = random.randint(1,3)
print("your choose: ")
if yours == 'rock':
    print(rock)
elif yours == 'paper':
    print(paper)
else:
    print(scissors)
if choose == 1:
    print(rock)
    choose = 'rock'
elif choose == 2:
    print(paper)
    choose = 'paper'
else:
    print(scissors)
    choose = 'scissors'
if yours == choose:
    print('Draw')
elif (yours =='rock' and choose == 'paper') or (yours =='paper' and choose =='scissors') or (yours == 'scissors' and choose =='rock'):
    print('You lose')
else:
    print('You win')
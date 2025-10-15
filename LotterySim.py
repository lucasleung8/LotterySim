import random

winningNumber = random.randint(1, 292000000)
start = 1
money = 0
jackpots = 0
print('Lets play the Powerball, with real odds!\n')

while start == 1:
  buy = input(f'You have spent ${money} so far and gotten {jackpots} jackpots. Buy a ticket? (y or n): ')
  match buy:
    case 'y':
      chosenNumber = random.randint(1, 292000000)
      money += 2
      if chosenNumber == winningNumber:
        print('Jackpot!')
        jackpots += 1
        start = 1
      else:
        print('Not a winner.')
        start = 1
    case 'n':
      print('Got it')
      exit()
    case _:
      print('Error please enter a valid answer')
      start = 1

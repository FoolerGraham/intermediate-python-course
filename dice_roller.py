def main():

  import random

  dice_rolls = 2
  dice_sum = 0

  if input("please enter your name: "):
    for i in range(0, dice_rolls):
      roll = random.randint(1, 6)
      dice_sum += roll
      if roll == 1:
        print(f'you rolled a {roll}, critical fail!')
      elif roll == 6:
        print(f'you rolled a {roll}, critical success!')
      else:
        print(f'You rolled {roll}')
    print(f'you have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
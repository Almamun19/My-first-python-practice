#This is a guess the number game.
import random
secretNumber=random.randint(1,20)
print('Iam thinking of a number between number 1 and 20.')
#Ask the player guess 6 times.
for guessesTaken in range(1,7):
 secretNumber=5
 print('Take a guess.')
 guess=int(input())
 if guess<secretNumber:
  print('Your guess is too low.')
 elif guess>secretNumber:
  print('Your guess is too high.')
 else:
  break #the condition is the correct guess
if guess==secretNumber:
 print('Good job! you guessed my number in' + str(guessesTaken) + 'guess!')
else:
 print('Nope! the number I was thinking of was' + str(secretNumber))
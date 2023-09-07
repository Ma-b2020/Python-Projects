import random
import math

#user input for least and highest number to be considered
lower_bound=int(input("Enter the minimum number:-"))
upper_bound=int(input("Enter the maximum number:-"))

count=0

#random number generated
x=random.randint(lower_bound,upper_bound)
min_guess=math.log((upper_bound-lower_bound+1),2)

print("You have ",round(min_guess)," chances to guess the number")

while count<min_guess:
    count+=1;
    guess=int(input("Guess a number:-"))

    #guess matches x
    if guess==x:
        print("Congratulations! You did it in ",count,"tries!")
        break
    elif x>guess:
        print("You guessed very low")
    elif x<guess:
        print("You guessed very high")

#if the number of guesses exceeds minimum guesses
if count>=min_guess:
    print('Sorry! You lost!')
    print("The number is ",x)
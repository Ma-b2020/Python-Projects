import random

words=['acceptance','honesty','priority','imagination','joy','gratitude','balance','discipline','motivation','belief','clarity','focus','determined']

#choosing a random word from the list
random_word=random.choice(words)

print("WELCOME to the WORD GUESSING GAME")
print("The length of the word is",len(random_word))

user_guesses=''
chances=10

print("Guess the characters:-")
while chances>0:
    wrong=0
    for char in random_word:
        if char in user_guesses:
            print(char, end=" ")
        else:
            print("_",end=" ")
            wrong+=1
    
    if wrong==0:
        print("Congratulations!You win!")
        print("The word is",random_word )
        break

    print()
    guess=input(print("Make a guess:-"))

    user_guesses+=guess

    if guess not in random_word:
        chances-=1;
        print("You have ",chances," more chances")

        if chances==0:
            print("Game Over! Better luck next time!")

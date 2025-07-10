answer = 6
print ("Guess a number between 1 and 10: ")
guess = int(input())
if guess == answer:
    print("You guessed the number correctly on your first try!")
else:
    if guess < answer:
        print("Please guess higher.")
    else:
        print("Please guess lower: ")
    guess = int(input())
    if guess == answer:
        print("🎉 Congratulations! You got the correct answer!")
    else:
        print("Sorry, you didn't guess the number.")
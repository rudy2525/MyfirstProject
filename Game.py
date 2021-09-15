hint = ["It is a part of a cat family", "It has black stripes", "It is a Carnivora", "it has four legs"]
my_word = "tiger"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guess = False
print("it is a animal")

while guess != my_word and not(out_of_guess):
    #if guess_count < guess_limit:
    guess = input("Enter your guess: ")
    if guess != my_word:
        if len(hint) == 0:
            out_of_guess = True
            break
        else:
            print(hint[len(hint) - 1])
            hint.pop()

        #guess_count += 1

if out_of_guess:
    print("You did not guess the word :(")
else:
    print("You have guessed the word!!")
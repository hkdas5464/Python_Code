# keybuttons
# `1234567899-=
# ~!@#$%^&*()_+

import random
def guess(X):
    random_number = random.randint(1,X)
    guess =0
    while guess != random_number:

        guess = int(input(f'Guess a number between 1 and {X}'))
        if guess < random_number:
            print(f"sorry ,guess again ,Too Low.{random_number}")
        elif guess> random_number:
            print(f"sorry ,guess again ,Too High.{random_number}")

    print(f"yey ,congracs , tou have guess the number {random_number} Cortrectly ")
guess(10)
# import random
# data= int(input("enter the digit"))



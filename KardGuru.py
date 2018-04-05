
print("Hello!")
user_rply = input("What is your name: ")
print(""+user_rply+", Wellcome to the KardGuru")
Hint = ("Hint:Do not excide the allowable score 21")

objctive =("The objective is to get as close to 21 without goin over")

print(objctive)

print(Hint)

print("Well Good Luck!!")

import random

dealer_cards = []

player_cards = []

while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1,11))
if len(dealer_cards) ==2:
        print("dealer has: x &", dealer_cards[1])


while len(player_cards) != 2:
     player_cards.append(random.randint(1, 11))
     if len(player_cards) == 2:
          print("You have ", player_cards)

if sum(dealer_cards) == 21:
        print("dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
        print("Dealer has busted")


while sum(player_cards) < 21:
        axn_taken = str(input("Do you wanna stay or hit? "))
        if axn_taken == "hit":
            player_cards.append(random.randint(1,11))
            print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
        else:
            print("The dealer has a total of " + str(sum(dealer_cards)) + " with", dealer_cards)
            print("You have a total of " + str(sum(player_cards)) + " with", player_cards )

            if sum(dealer_cards) > sum(player_cards):
                print("Ooops, Dealer wins!!")
                print("Game Over")
            else:
                print("Yeah!! You've Won!!")
                print("Game Over")
                break


if sum(player_cards) > 21:
        print("You BUSTED! dealer wins.")

elif sum(player_cards) == 21:
        print("You are a GURU! You win!! 21")










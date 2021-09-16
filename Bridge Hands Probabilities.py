import random


def handGenerator(myHand, partnerHand = None):
    if partnerHand == None: # This block will generate myHand
        for i in range(13):
            card = random.randint(1, 13)
            suit = random.randint(1, 4)

            while card in myHand[suit]:
                card = random.randint(1, 13)
                suit = random.randint(1, 4)

            myHand[suit].append(card)
            myHand[suit].sort()

        return myHand

    else:  # This block will generate partnerHand
        for i in range(13):
            card = random.randint(1, 13)
            suit = random.randint(1, 4)

            while (card in myHand[suit]) or (card in partnerHand[suit]):
                card = random.randint(1, 13)
                suit = random.randint(1, 4)

            partnerHand[suit].append(card)
            partnerHand[suit].sort()

        return partnerHand


def calcPoints(hand):
    totalPoints = 0

    for suit in hand.keys():
        for card in hand[suit]:
            if card == 1:
                totalPoints += 4
            elif card == 13:
                totalPoints += 3
            elif card == 12:
                totalPoints += 2
            elif card == 11:
                totalPoints += 1

        if len(hand[suit]) == 0:
            totalPoints += 5
        elif len(hand[suit]) == 1:
            totalPoints += 2
        elif len(hand[suit]) == 2:
            totalPoints += 1

    return totalPoints


def printHand(hand):
    cardNames = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    cardSuits = {1: "Spades", 2: "Clubs", 3: "Hearts", 4: "Diamonds"}

    for suit in hand.keys():
        for card in hand[suit]:
            if card in cardNames.keys():
                print(cardNames[card], "of", cardSuits[suit], end=", ")

            else:
                print(card, "of", cardSuits[suit], end=", ")
    print("\n")


def main():
    userInput = "Y"

    while userInput == "Y":
        myHand = {1: [], 2: [], 3: [], 4: []}

        myHand = handGenerator(myHand)

        trials = 1000

        score = {"Pass": [], "Part Score": [], "Game": [], "Small Slam": [], "Grand Slam": []}

        for i in range(trials):
            partnerHand = {1: [], 2: [], 3: [], 4: []}
            partnerHand = handGenerator(myHand, partnerHand)

            partnerPoints = calcPoints(partnerHand)
            myPoints = calcPoints(myHand)
            totalPoints = partnerPoints + myPoints

            if totalPoints < 20:
                score["Pass"].append(totalPoints)
            elif totalPoints <= 25:
                score["Part Score"].append(totalPoints)
            elif totalPoints <= 31:
                score["Game"].append(totalPoints)
            elif totalPoints <= 35:
                score["Small Slam"].append(totalPoints)
            elif totalPoints > 36:
                score["Grand Slam"].append(totalPoints)

        print("Here is your hand:")
        printHand(myHand)

        print("Here are your probabilities:")

        for key in score.keys():
            print(key + ":", "{:.1f}%".format(len(score[key])/trials * 100))

        print()
        userInput = input("Try another hand? [Y/N]: ").upper()


if __name__ == "__main__":
    main()

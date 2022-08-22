import random

def trapezoids(quantity):
    i = 0
    questionTotal = ""
    for i in range(quantity):
        randArea = random.randint(50, 150)
        randB1 = random.randint(1, 10)
        randB2 = random.randint(1, 10)

        answer = (2 * randArea) / (randB1 + randB2)

        questionText = "\nFind the heights of a trapezoid if:\n Area (A)=" + str(randArea) + "cm^2\n Base1 (B1)=" + str(randB1) + "cm\n Base2 (B2)=" + str(randB2) + "cm\n\nAnswer=" + str(
            round(answer, 2))
        questionTotal = questionTotal + questionText

        i+=1

    return questionTotal


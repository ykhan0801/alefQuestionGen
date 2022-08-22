import random

def triangle(quantity):
    i = 0
    questionTotal = ""
    for i in range(quantity):
        randBase = random.randint(1, 10)
        randHeight = random.randint(1, 10)
        randMultiplier = random.randint(2, 10)

        answer = randMultiplier * randMultiplier

        questionText = "\n\nA Triangle has a base of " + str(randBase) + "m and a height of " + str(randHeight) + "m. The dimensions are multiplied by " + str(
            randMultiplier) + ".\n What effect would have on the area?\nAnswer=" + str(answer)
        questionTotal = questionTotal + questionText

        i += 1

    return questionTotal

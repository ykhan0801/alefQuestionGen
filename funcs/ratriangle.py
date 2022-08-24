import random
import math

def ratriangle(quantity):
    i = 0
    questionTotal = ""
    for i in range(quantity):
        randBase = random.randint(1, 10)
        randHeight = random.randint(1, 10)

        answer = round(math.sqrt((randBase*randBase)+(randHeight*randHeight)), 2)

        questionText = "\n\nA triangle has a base of " + str(randBase) + "m and a length of " + str(randHeight) + "m.\nWhat is the length of the third side of this trianlge?\nAnswer=" + str(answer)
        questionTotal = questionTotal + questionText

        i += 1

    return questionTotal

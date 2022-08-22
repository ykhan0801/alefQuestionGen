import random

def pyramids(quantity):
    i = 0
    questionTotal = ""
    for i in range(quantity):
        randPerimeter = random.randint(1, 10)
        randHeight = random.randint(1, 10)
        randArea = random.randint(3, 10)

        answer = (0.5 * randPerimeter * randHeight) + randArea

        questionText = "\n\nA Triangular pyramid pizza box has a slant height of " + str(randHeight) + " meters (l). The equilateral triangular base has a perimeter of " + str(
            randPerimeter) + " meters (p) and an area of " + str(randArea) + " (B) square meters. Find the surface area of the triangular pyramid? \nAnswer=" + str(answer)
        questionTotal = questionTotal + questionText

        i += 1

    return questionTotal

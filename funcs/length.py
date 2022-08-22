import random

def length(quantity):
    i = 0
    questionTotal = ""
    for i in range(quantity):
        randlength = random.randint(1, 10)

        answer = randlength * 100

        questionText = "\n\nSheikha has a ribbon that is " + str(randlength) + "m long (l). What is the length of the ribbon in cm?\nAnswer=" + str(answer)
        questionTotal = questionTotal + questionText

        i+=1

    return questionTotal
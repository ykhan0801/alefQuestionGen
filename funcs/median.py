import random
import statistics

def median(quantity):
    i = 0
    questionTotal = ""
    for i in range(quantity):
        randomlist = []
        for i in range(0, 7):
            n = random.randint(1, 30)
            randomlist.append(n)

        answer = statistics.median(randomlist)

        questionText = "\n\nThe table shows the number of girls in 8 classes. Find the median: \n" + str(randomlist) + "\nAnswer= " + str(answer)
        questionTotal = questionTotal + questionText

        i+=1

    return questionTotal

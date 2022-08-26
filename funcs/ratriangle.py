import random
import math


def ratriangle(quantity):
    i = 0
    svgList = []
    questionTotal = ""
    for i in range(quantity):
        randBase = random.randint(5, 10)
        randHeight = random.randint(5, 10)

        baseCoord = str((randBase*10) + 50)
        height = str((randHeight*10) + 50)

        answer = round(math.sqrt((randBase*randBase)+(randHeight*randHeight)), 2)

        questionText = "\n\nA triangle has a base of " + str(randBase) + "m and a length of " + str(randHeight) + "m.\nWhat is the length of the third side of this trianlge?\nAnswer=" + str(answer)
        questionTotal = questionTotal + questionText

        svgList.append("""
        <svg xmlns="http://www.w3.org/2000/svg" width="400" height="400">
        <line x1="50" y1="350" x2="350" y2="350" stroke="white" stroke-width="3"/>
        <line x1="50" y1="350" x2="50" y2="50" stroke="white" stroke-width="3"/>
        <line x1="50" y1="50" x2="350" y2="350" stroke="white" stroke-width="3"/>
        <text x="160" y = "340" class="base" stroke="white" fill="white" font-family="Arial"> """ + str(randBase) + """"cm </text>
        <text x="60" y = "200" class="height" stroke="white" fill="white" font-family="Arial"> """ + str(randHeight) + """"cm </text>
        <text x="190" y = "170" class="base" stroke="red" fill="red" font-family="Arial"> ? </text>
        </svg>""")

        i += 1

    return questionTotal, svgList

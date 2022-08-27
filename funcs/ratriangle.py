import random
import math


def ratriangle(quantity):
    i = 0
    svgList = []
    questionTotal = ""
    for i in range(quantity):
        randBase = random.randint(5, 10)
        randHeight = random.randint(5, 10)

        base = str((randBase*25) + 50)
        base = '"{}"'.format(base)
        height = str(400 - ((randHeight*25) + 50))
        height = '"{}"'.format(height)

        answer = round(math.sqrt((randBase*randBase)+(randHeight*randHeight)), 2)

        questionText = "\n\nA triangle has a base of " + str(randBase) + "m and a length of " + str(randHeight) + "m.\nWhat is the length of the third side of this trianlge?\nAnswer=" + str(answer)
        questionTotal = questionTotal + questionText

        svgList.append("""
        <svg xmlns="http://www.w3.org/2000/svg" width="400" height="400">
        <line x1="50" y1=""" + height + """ x2=""" + base + """ y2="350" stroke="white" stroke-width="3"/>
        <line x1="50" y1="350" x2="50" y2=""" + height + """ stroke="white" stroke-width="3"/>
        <line x1="50" y1="350" x2=""" + base + """ y2="350" stroke="white" stroke-width="3"/>
        <text x="90" y = "370" class="base" stroke="white" fill="white" font-family="Arial"> """ + str(randBase) + """"cm </text>
        <text x="5" y ="260" class="height" stroke="white" fill="white" font-family="Arial"> """ + str(randHeight) + """"cm </text>
        <text x="200" y = "200" class="base" stroke="red" fill="red" font-family="Arial"> ? </text>
        </svg>""")

        i += 1

    return questionTotal, svgList

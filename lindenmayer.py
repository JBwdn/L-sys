# Dependencies
from turtle import *

# TODO: system to save each bit in the resulting paragraph as a vector and visualise using matplotlib.pyplot.quiver

# Parameters:
variables = ["X", "F"]
constants = ["[", "]", "+", "-"]
axiom = "X"
rules = ["XF+[[X]-X]-F[-FX]+X)", "FFF"]
N = 8
length = 5
lengthChange = 0
angle = 18
position = "bottom" # middle/bottom
mode = "single" # single/continuous

# Function: Generate L-system
def generate(sentence, rules, constants):
    nextSentence = ""
    for i in range(0,len(sentence)):
        bit = sentence[i]
        # Check if bit is in constants or variables:
        if bit not in constants:
            for j in range(0,len(rules)):
                if bit == rules[j][0]:
                    nextSentence += rules[j][1:]
        else:
            nextSentence += bit
    return nextSentence

# Function: Draw using turtle
def turtleDraw(commandString, variables, length, angle):
    savedCoords = []
    savedDir = []
    pushcount = 0
    for i in commandString:
        if i in variables:
            forward(length)
        elif i == "-":
            left(angle)
        elif i == "+":
            right(angle)
        elif i == "[":
            savedCoords.append(pos())
            savedDir.append(heading())
        elif i == "]":
            penup()
            setpos(savedCoords[-1])
            setheading(savedDir[-1])
            del savedCoords[-1]
            del savedDir[-1]
            pushcount += 1
            pendown()

# Function: Initialise canvas
def init(pos):
    hideturtle()
    penup()
    if pos == "bottom":
        right(90)
        forward(350)
        left(180)
    else:
        left(90)
    pendown()

# Execute:
init(position)
paragraph = axiom
if mode == "single":
    for i in range(N):
        newparagraph = generate(paragraph, rules, constants)
        paragraph = newparagraph
    turtleDraw(paragraph, variables, length, angle)
elif mode == "continuous":
    for i in range(N):
        turtleDraw(paragraph, variables, length, angle)
        newparagraph = generate(paragraph, rules, constants)
        paragraph = newparagraph
        length += lengthChange

print(paragraph)
done()

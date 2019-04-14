# Dependencies
from turtle import *

# TODO: need to pull and push direction as well as position with [ and ] bits - i think this is the error

# Parameters:
variables = ["X", "F"]
constants = ["[", "]", "+", "-"]
axiom = "X"
rules = ["XF+[[X]-X]-F[-FX]+X", "FFF"] #(X → F+[[X]-X]-F[-FX]+X), (F → FF)
N = 6
length = 5
lengthChange = 0
angle = 25
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
        elif i == "]":
            penup()
            setpos(savedCoords[pushcount])
            pushcount += 1
            pendown()

# Function: Initialise
def init(pos):
    #begin_fill()
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

done()

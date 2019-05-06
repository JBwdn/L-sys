#!/usr/bin/env python
import turtle

# Parameters:
variables = ["0", "1"]
constants = ["+", "-", "[", "]"]
axiom = "1"
rules = ["11+0++0-1--11-0+", "0-1+00++0+1--1-0"]
N = 4
length = 10
lengthChange = 0
angle = 60
position = "middle" # middle/low/lowright/lowleft
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
            turtle.forward(length)
        elif i == "-":
            turtle.left(angle)
        elif i == "+":
            turtle.right(angle)
        elif i == "[":
            savedCoords.append(turtle.pos())
            savedDir.append(turtle.heading())
        elif i == "]":
            turtle.penup()
            turtle.setpos(savedCoords[-1])
            turtle.setheading(savedDir[-1])
            del savedCoords[-1]
            del savedDir[-1]
            pushcount += 1
            turtle.pendown()

# Function: Initialise canvas
def init(pos):
    turtle.hideturtle()
    turtle.penup()
    if pos == "low":
        turtle.right(90)
        turtle.forward(350)
        turtle.left(180)
    elif pos == "middle":
        turtle.left(90)
    elif pos == "lowright":
        turtle.right(90)
        turtle.forward(350)
        turtle.left(90)
        turtle.forward(350)
        turtle.left(90)
    elif pos == "lowleft":
        turtle.right(90)
        turtle.forward(350)
        turtle.right(90)
        turtle.forward(350)
        turtle.left(180)
    turtle.pendown()

# Main Function:
if __name__ == "__main__":
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
    turtle.done()

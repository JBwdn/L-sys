#!/usr/bin/env python
import lindenmayer

variables = ["0", "1"]
constants = ["+", "-", "[", "]"]
axiom = "1-1-1-1"
rules = ["11-1+1+11-1-1+1"]
N = 3
length = 7
angle = 90
position = "lowleft"

if __name__ == "__main__":
    lindenmayer.main(position, axiom, N, rules, constants, length, angle)

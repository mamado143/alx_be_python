#!/usr/bin/python3
pattern = int (input ("Enter the size of the pattern: "))
i = 0

while i < pattern:
    for j in range(pattern):
        print("*", end="")
    print()
    i+=1

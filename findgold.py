#!/usr/bin/env python3

import sys

gold = (1 + 5 ** 0.5) / 2

if len(sys.argv) > 1:
    closestNum = int(sys.argv[1])
else:
    closestNum = 0
    while closestNum <= 0:
        closestNum = int(input("\nEnter the number and I'll find the closest golden ratio: ") or 0) 
precision = int(input(f"\nEnter the level of precision(up to {len(str(gold))-2} decimal places by default): ") or len(str(gold))-2)

if closestNum > 3000:
    print("\n...Big number, may take a moment to compute...")

gold = ("".join(str(gold)[:precision+2]))

results = []
for x in range(1, closestNum+1):
    for y in range(1, x+1):
        diviRes = x / y
        vars = [[x, y], diviRes]
        results.append(vars)

found = []
foolsGold = float(gold) - float(results[0][1])
for x in range(1, len(results)):
    foundGold = float(gold) - float(results[x][1])
    if foundGold > 0 and foundGold < foolsGold:
        foolsGold = foundGold
        found.append(results[x][0])
print(f"\n** The closest golden ratio is {found[-1][0]} / {found[-1][1]} = {found[-1][0] / found[-1][1]} **\n")
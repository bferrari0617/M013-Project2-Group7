#!/usr/bin/env python3
#ECS 101
#Project 2 part 3
#Timothy Liu
import random
c1avg = 9
c1std = 3
c2avg = 7
c2std = 5
c3avg = 11
c3std = 7
def c1():
	return random.normalvariate(c1avg, c1std)
def c2():
	return random.normalvariate(c2avg, c2std)
def c3():
	return random.normalvariate(c3avg, c3std)
def returnhappy(n):
	if (n == 0):
		happy = c1()
	elif (n == 1):
		happy = c2()
	else:
		happy = c3()
	return happy

def eGreeydy(e):
	result = 0
	#First 3 day:
	firstThreeDays = []
	firstThreeDays.append(c1())
	firstThreeDays.append(c2())
	firstThreeDays.append(c2())
	best = firstThreeDays.index(max(firstThreeDays))
	result += sum(firstThreeDays)
	# calculate assign for rest 297 days:
	bestcafeDays = 297 * e // 100
	restDays = 297 - bestcafeDays
	# go to the favorate cafe e% times:
	for i in range(bestcafeDays):
		happy = returnhappy(best)
		result += happy
	# go to the random cafe rest times:
	for i in range (restDays):
		cafe = random.randrange(3)
		happy = returnhappy(cafe)
		result += happy
	return result
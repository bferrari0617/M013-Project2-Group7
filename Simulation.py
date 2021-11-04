import random

def explore_only() -> int:
    h1 = 0
    h2 = 0
    h3 = 0
    i = 0
    while i < 100:
        h1 += random.normalvariate(9, 3)
        i += 1
    while i < 200:
        h2 += random.normalvariate(7, 5)
        i += 1
    while i < 300:
        h3 += random.normalvariate(11, 7)
        i += 1
    return int(h1 + h2 + h3)


h = [random.normalvariate(9, 3), random.normalvariate(7, 5), random.normalvariate(11, 7)]

def exploitOnly() -> float:
	result = 0
	best = h.index(max(h))

	if best == 0:
		m, d = 9, 3
	elif best == 1:
		m, d = 7, 5
	else:
		m, d = 11, 7

	for item in h:
		result += item
	for i in range(297):
		result += random.normalvariate(m, d)

	return result

#!/usr/bin/env python3
#ECS 101
#Project 2 part 3
#Timothy Liu

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

def simulation(t,e):
	c1a = 9
	c2a = 7
	c3a = 11
	c1s = 3
	c2s = 5
	c3s = 7

	n = 300 * (e/100/3)


	Op_happy = 300*(max(c1a,c2a,c3a))

	ex_explore = 100*c1a + 100*c2a + 100*c3a
	ex_exploit =  c1a + c2a + c3a + 297*(max(c1a,c2a,c3a))
	ex_eGreedy = (100-e)/100 * 300 * (max(c1a,c2a,c3a)) + c1a * n + c2a * n + c3a * n

	regret_explore = Op_happy - ex_explore
	regret_exploit = Op_happy - ex_exploit
	regret_eGreddy = Op_happy - ex_eGreedy

	total_explore = 0
	total_exploit = 0
	total_eGreedy = 0
	for i in range (0,t):
		total_explore += explore_only()
		total_exploit += exploitOnly()
		total_eGreedy += eGreeydy(e)


	aver_explore = total_explore / t
	aver_exploit = total_exploit / t
	aver_eGreedy = total_eGreedy / t

	print("Optimum happiness: ",Op_happy);
	print("Expected total happiness for Exploit Only: ",ex_exploit);
	print("Expected total happiness for Explore Only: ", ex_explore);
	print("Expected total happiness for eGreedy: ", ex_eGreedy);
	print("Average total happiness for Exploit Only: ", aver_exploit);
	print("Average total happiness for Explore Only: ", aver_explore);
	print("Average total happiness for eGreedy: ", aver_eGreedy);
	print()

print("trails: 1000; e: 36%")
simulation(1000,36)
print("trails: 10000; e: 36%")
simulation(10000,36)
print("trails: 100000; e: 36%")
simulation(100000,36)

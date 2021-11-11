#ECS 101 Project 2 Group 7
#Simulation.py
#made by Bennett Ferrari, Eddie Garcia, Junjie Zheng, and Timothy Liu

import random
#Bennett Ferrari's part
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




#Eddie Garcia's part
def exploitOnly() -> float:
	h = [random.normalvariate(9, 3), random.normalvariate(7, 5), random.normalvariate(11, 7)]
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
#Timothy Liu‘

#The number provided from class:
c1avg = 9
c1std = 3
c2avg = 7
c2std = 5
c3avg = 11
c3std = 7
#Some helper function, return the happiness value each time by using the given num
def c1():
	return random.normalvariate(c1avg, c1std)
def c2():
	return random.normalvariate(c2avg, c2std)
def c3():
	return random.normalvariate(c3avg, c3std)
#eGreedy(e) starts here, input: e -> is percentage, e%
def eGreedy(e):
	#First Three day, go to each cafeteria and get the happiness value
	result = 0 #Result
	happiness = [] #Empty list to put happy score in
	happiness.append(c1()) #append happiness into the list
	happiness.append(c2())
	happiness.append(c3())
	result += sum(happiness) #add three days' happyiness point
	#initial int visit times. Initial from one because you already viisted each cafeteria onece
	c1n = 1
	c2n = 1
	c3n = 1
	#The rest 297 days
	for i in range (297):#Loop starts here
		#Generate a random number 0 to 100
		r = 100 * random.random()
		#Generate a random number 0 to 2(0,1,2,3)
		x = random.randrange(3)
		#If the random number r is smaller than e, pick a random cafeteria
		if (r < e):
			#according the random number x, if x is 0 go to cafeteria one
			if (x == 0):
				c1n += 1 #add visit times
				c1h = c1() #get happiness core using helper function
				happiness[0] = (happiness[0] + c1h) / c1n #modify the happiness score for this cafeteria so far
				result += c1h #add the happiness score to the total result
			elif (x == 1):
			# if random num x is 1, go to the cafeteria two
				c2n += 1 
				c2h = c2()
				happiness[1] = (happiness[1] + c2h) / c2n
				result += c2h
			else:
			#the last situation is random num x is three, go to the cafeteria three
				c3n += 1
				c3h = c3()
				happiness[2] = (happiness[2] + c3h) / c3n
				result += c3h
		else:
		#Otherwise, go to the cafeteria earn the best happiness so far
			y = happiness.index(max(happiness))#from the happiness list, get the index has the highest number is the best happiness cafeteria so far
			#If first number is the highest, go to the cafeteria one
			if (y == 0):
				c1n += 1 #add visit time
				c1h = c1() #get happiness score by using helper function
				happiness[0] = (happiness[0] + c1h) / c1n #update the average happiness score 
				result += c1h # add to result
			#if the second number is the highest, go to the cafeteria two
			elif (y == 1):
				c2n += 1
				c2h = c2()
				happiness[1] = (happiness[1] + c2h) / c2n
				result += c2h
			#The last situation, the last num is the highest in the list, go to the cafeteria three
			else:
				c3n += 1
				c3h = c3()
				happiness[2] = (happiness[2] + c3h) / c3n
				result += c3h
		
	#Return the happiness score
	return result

#Junjie Zheng's part
#simulation(t,e) int t -> is the times of trail; int e -> is the given percentage(0-100) use for eGreedy(e)
def simulation(t,e):
	#The given number for the project, avg num & std diviation
	c1a = 9
	c2a = 7
	c3a = 11
	c1s = 3
	c2s = 5
	c3s = 7
	
	# calculate the expect total happiness
	# n is the times go to each cafeteria during the 300 days
	n = 300 * (e/100/3)

	#Optimum happiness
	Op_happy = 300*(max(c1a,c2a,c3a))

	#Calculate the expect total happiness score from given average happiness score
	ex_explore = 100*c1a + 100*c2a + 100*c3a
	ex_exploit =  c1a + c2a + c3a + 297*(max(c1a,c2a,c3a))
	ex_eGreedy = (100-e)/100 * 300 * (max(c1a,c2a,c3a)) + c1a * n + c2a * n + c3a * n
	
	#Calculate the regreat by deduct optimum happiness with expect happiness score
	regret_explore = Op_happy - ex_explore
	regret_exploit = Op_happy - ex_exploit
	regret_eGreedy = Op_happy - ex_eGreedy

	#initial the some integer, initial value is 0
	total_explore = 0
	total_exploit = 0
	total_eGreedy = 0

	#initial another integers here, initial value is 0
	total_regret1 = 0
	total_regret2 = 0
	total_regret3 = 0
	
	#for loop
	#loop runs t times, t is the input value of this function
	for i in range (0,t):
		#runs the function wrote by other teamate
		h1 = explore_only()
		h2 = exploitOnly()
		h3 = eGreedy(e)
		
		#Add the happiness return by each function to the total num
		total_explore += h1
		total_exploit += h2
		total_eGreedy += h3
		
		#Add the regreat
		total_regret1 += (Op_happy - h1)
		total_regret2 += (Op_happy - h2)
		total_regret3 += (Op_happy - h3)
	#The end of for loop
	
	#calculate the average happiness score
	aver_explore = total_explore / t
	aver_exploit = total_exploit / t
	aver_eGreedy = total_eGreedy / t
	#calculate the average regret score
	aver_regret1 = total_regret1 / t
	aver_regret2 = total_regret2 / t
	aver_regret3 = total_regret3 / t
	
	#print results:
	print("Optimum happiness: ",Op_happy);
	print("Expected total happiness for Exploit Only: ",round(ex_exploit));
	print("Expected total happiness for Explore Only: ", round(ex_explore));
	print("Expected total happiness for eGreedy: ", round(ex_eGreedy));
	print("Expected regret for Exploit Only: ", round(regret_exploit));
	print("Expected regret for Explore Only: ", round(regret_explore));
	print("Expected regret for eGreedy: ", round(regret_eGreedy));
	print("Average total happiness for Exploit Only: ", round(aver_exploit));
	print("Average total happiness for Explore Only: ", round(aver_explore));
	print("Average total happiness for eGreedy: ", round(aver_eGreedy));
	print("Average regret for Exploit Only: ", round(aver_regret2));
	print("Average regret for Explore Only: ", round(aver_regret1));
	print("Average regret for eGreedy: ", round(aver_regret3));
	print()
	#The end of simulation()
	
#Print Results:
print("trials: 100; e: 12%")
simulation(100,12)
print("trials: 1000; e: 12%")
simulation(1000,12)
print("trials: 10，000; e: 12%")
simulation(10000,12)
print("trials: 100，000; e: 12%")
simulation(100000,12)


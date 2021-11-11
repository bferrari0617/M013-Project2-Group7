# M013--Project-2--Group-7

This is project 2 for ECS 101
Simulation.py contains four functions:
- Exploit()

- Explore()

- eGreedy(e)
should be given a percentage value for e.  e% of the time you will pick a random cafeteria to go to and generate a happiness value based on the normal distribution of that cafeteria. The other 100-e% of the time you will generate a random number from 0 to 100. If the number is smaller than the e given, you will go to a random cafeteria. Otherwise go to the current cafeteria has the highest average happiness score.

- Simulation(t,e)
run a simulation of each of the three algorithms. The function should take as input the number of trials (t) to run. Then, it will run each program (exploitOnly, exploreOnly, and eGreedy) and print the following information

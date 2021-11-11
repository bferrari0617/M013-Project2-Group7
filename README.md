# M013--Project-2--Group-7

This is project 2 for ECS 101
This will run a simulation based on the multi-armed bandit problem. Pretend you are doing a study abroad program for 300 days. You get a meal at one of three cafeterias (C1, C2, and C3) each of the days that you are there. You want to maximize the happiness you get eating at these cafeterias. There is a normal distribution describing the happiness that you will derive from each cafeteria. This is given as the average happiness value (H1, H2, H3) and the standard deviation (D1, D2, D3). These distributions are hidden from you. You don’t know yet how much you might like each cafeteria.

Simulation.py contains four functions:
- Exploit()

- Explore()

- eGreedy(e)
should be given a percentage value for e.  e% of the time you will pick a random cafeteria to go to and generate a happiness value based on the normal distribution of that cafeteria. The other 100-e% of the time you will generate a random number from 0 to 100. If the number is smaller than the e given, you will go to a random cafeteria. Otherwise go to the current cafeteria has the highest average happiness score.

- Simulation(t,e)
run a simulation of each of the three algorithms. The function should take as input the number of trials (t) to run. Then, it will run each program (exploitOnly, exploreOnly, and eGreedy) and print the following information

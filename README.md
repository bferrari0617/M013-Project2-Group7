# M013--Project-2--Group-7

This is project 2 for ECS 101
This will run a simulation based on the multi-armed bandit problem. Pretend you are doing a study abroad program for 300 days. You get a meal at one of three cafeterias (C1, C2, and C3) each of the days that you are there. You want to maximize the happiness you get eating at these cafeterias. There is a normal distribution describing the happiness that you will derive from each cafeteria. This is given as the average happiness value (H1, H2, H3) and the standard deviation (D1, D2, D3). These distributions are hidden from you. You don’t know yet how much you might like each cafeteria.

Simulation.py contains four functions:
- exploitOnly()
 This function does not take any parameters. It visits each of the three cafes on three different days and calculates happiness based on the normal distribution with the given mean and standard deviation. The function finds the index of the cafe with the highest happiness value, then uses an 'if elif else' to save the mean and standard deviation of the cafe with the highest happiness value. The first for loop adds the first three days of cafe to the total happiness. The second for loop uses the saved values for mean and standard deviation from the cafe with the highest happiness value to simulate visting that cafe for 297 more days (for a total of 300 days), and adds the happiness values generated from those 297 days to the total happiness. Lastly, the function returns the total happiness.
 
- exploreOnly()
This function visits each of three cafes for 100 days and saves the happiness values generated for each day to a variable. The happiness value is based on the normal distribution calculated with the given mean and standard deviation for each cafe. The function returns the sum of all happiness generated.

- eGreedy(e)
should be given a percentage value for e.  e% of the time you will pick a random cafeteria to go to and generate a happiness value based on the normal distribution of that cafeteria. The other 100-e% of the time you will generate a random number from 0 to 100. If the number is smaller than the e given, you will go to a random cafeteria. Otherwise go to the current cafeteria has the highest average happiness score.

- Simulation(t,e)
run a simulation of each of the three algorithms. The function should take as input the number of trials (t) to run. Then, it will run each program (exploitOnly, exploreOnly, and eGreedy) and print the following information

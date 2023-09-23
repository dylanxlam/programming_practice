# File: Collatz.py
# Description: A basic 2D Triangle class
# Student Name: Dylan Lam
# Student UT EID: DXL85
# Course Name: CS 313E
# Unique Number: 52605



import sys

# Input: an integer start point for a Collatz sequence
# Output: a tuple (s, w) where s is the step distance from start to 1,
# and w is the amount of work required to calculate this step distance
# given previous calculations
def step_dist(start):
    s = 0
    w = 0
    n = start

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        s += 1
        w += 1
        
        for key in step_dist:
            if key == n:
                w += step_dist[key][1]
    
    step_dist[start] = (s, w)
    
    return (s, w)

def main():
    # You shouldn't have to change anything below this line
    queries = [int(k) for k in sys.stdin.readlines()]
    for q in queries:
        actual_steps, work_steps = step_dist(q)
        print(str(actual_steps) + ' ' + str(work_steps))

if __name__ == "__main__":
    main()

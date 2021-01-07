'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
T = int(input())
for i in range(T):
    cost_1 , cost_2 = (0,0)
    green, purple = map(int, input().split())
    N = int(input())
    for j in range(N):
        first , second = map(int, input().split())
        cost_1 += green * first + purple * second
        cost_2 += purple * first + green * second
    print(min(cost_1, cost_2))

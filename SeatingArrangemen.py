'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
#Write your code her
t=int(input())
for i in range(t):
     n=int(input())
     position=""
     if(n%6==0 or n%6==1):
          position="WS"
     elif(n%6==2 or n%6==5):
          position="MS"
     else:
          position="AS"
     if(n%12==0):
          seat=n-11
     else:
          startingPoint=((n//12)*12)+1
          lastPoint=((n//12)+1)*12
          big=startingPoint+lastPoint
          seat=big-n
     print(seat,position)

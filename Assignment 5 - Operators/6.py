'''Write a python script which takes a three digit number from the user and displays
only its middle digit'''
print('Enter Three digit number 000 to 999 :')
d = int(input())
middle = int(str(d)[1:-1:])
print(middle)
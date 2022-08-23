'''Write a python script which takes a three digit number from the user and displays only its first digit.'''
print('Enter Three digit number')
a = int(input())
first = int(str(a)[-1:])
print(first)

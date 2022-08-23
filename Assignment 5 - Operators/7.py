'''Write a python script which takes a three digit number from the user and displays only its last digit.'''
print("Enter Three digit number 000 to 999 :")
d = int(input())
last_digit = int(str(d)[-1:])
print(last_digit)
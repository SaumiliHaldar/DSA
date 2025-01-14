"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""


maxm = int(input("Enter the max number : "))
print(list(range(1, maxm, 2)))
"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""


maxm = int(input("Enter the max number : "))
odd_numbers = []
for i in range(1, maxm):
    if i % 2 == 1:
        odd_numbers.append(i)
print("Odd numbers: ", odd_numbers)
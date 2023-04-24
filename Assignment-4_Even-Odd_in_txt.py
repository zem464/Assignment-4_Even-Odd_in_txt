# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 4

# Problem 1 - Even and Odd numbers in text files

# Create a method to process the text files
def integers():
    # Create a text file named for the 20 integers, even integers, and odd integers
    with open("numbers.txt") as numbers_input, open("even.txt", "a") as even_num, open("odd.txt", "a") as odd_num:
        
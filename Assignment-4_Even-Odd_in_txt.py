# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 4

# Problem 1 - Even and Odd numbers in text files

# Create a method to process the text files
def integers():
    # Create a text file named for the 20 integers, even integers, and odd integers
    with open("numbers.txt") as numbers_input, open("even.txt", "a") as even_num, open("odd.txt", "a") as odd_num:
        # Read the text line by line
        for line in numbers_input:
            # Convert string to integer
            if line.strip:
                int_input = int(line)
                # Check if line is even,
                if int_input % 2 == 0:
                    # Write to even.txt
                    even_num.write(str(int_input) + "\n")
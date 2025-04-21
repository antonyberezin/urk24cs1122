# Function to check if the number is odd or even and perform required operation
def process_numbers(numbers):
    oddlist = []
    evenlist = []
    
    for num in numbers:
        if num % 2 == 0:  # Even number
            evenlist.append(num ** 3)
        else:  # Odd number
            oddlist.append(num ** 2)
    
    return oddlist, evenlist


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


oddlist, evenlist = process_numbers(numbers)


print("Original List:", numbers)
print("Odd List:", oddlist)
print("Even List:", evenlist)

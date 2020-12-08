# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def get_list_of_numbers(range_higher: int, range_lower: int = 0) -> list:
    """
    Function returns a list of numbers that are multiples of 3 and 5
    """
    # Place holder
    numbers_list = []
    # Loop through numbers and add 1 to include actual number.
    for number in range(range_lower,range_higher + 1):

        if ( number % 3 == 0 ) and ( number % 5 == 0):
            numbers_list.append(number)
    
    return numbers_list

if __name__ == "__main__":
    numbers_list = get_list_of_numbers(range_higher = 1000)
    total = sum(numbers_list)
    print(total)
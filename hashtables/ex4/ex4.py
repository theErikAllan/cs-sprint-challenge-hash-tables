def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # We initialize the dictionary for keeping track of the positive and negative integers
    num_dict = {}

    # We initialize the output array
    result = []

    # We loop through the numbers in the input array and add the positive integers to the dictionary
    for num in a:
        if num > 0:
            num_dict[num] = True
        
    # We loop through the numbers in the input array again, but this time we check if the negative integers have corresponding positive values in the dictionary
    for num in a:    
        if num < 0 and abs(num) in num_dict:
            # We append the positive integer to the output array
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # We initialize a dictionary to track the weights and their corresponding indices in the weights list
    index_dict = {}

    # We create conditionals for two base cases
    # If the list of weights is 1 or less, we return None since we have nothing to add to to hit the limit
    if len(weights) <= 1:
        return None

    # If the list of weights has 2 weights, we just check if the sum is equal to the limit and output the indices if they are
    if len(weights) == 2:
        sum_of_weights = weights[0] + weights[1]
        if sum_of_weights == limit:
            return (1, 0)
        else:
            return None

    # If the array passes the base cases, we use a for loop to add the weights to the index dictionary
    for index in range(len(weights)):
        index_dict[weights[index]] = index

    # Then we loop through the index dictionary
    for weight in index_dict:
        # For each weight, we calculate the difference between the limit and the weight
        difference = limit - weight

        # Then we check to see if the difference is in the index dictionary AND in case there are duplicates (i.e. [4, 4]), we make sure we're not looking at the same value that we're checking
        if difference in index_dict and index_dict[difference] != index_dict[weight]:
            # If we find the two weights that sum together to equal the limit, we output the result in a tuple
            return (index_dict[difference], index_dict[weight])

    return None

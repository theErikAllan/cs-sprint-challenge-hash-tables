def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # 'limit' is just a number
    # 'weights' is just an array of numbers
    # loop through 'weights' to find sum of numbers equal to 'limit'
    # treat function like trying to solve for a missing variable 
    # b = c - a, weight2 = limit - weight1
    # return a tuple, where each element is the index of the item weight in 'weights' list
    # tuple needs to be in format of (index of higher 'weight', index of lower 'weight')
    # return None if pair doesn't exist that adds to sum ('limit')

    weights_dict = {}
    index = 0

    for weight in weights:
        weights_dict[weight] = index
        index += 1

    for i in range(length):
        missing_weight = limit - weights[i]
        print("This is weights dict: ", weights_dict)

        if missing_weight in weights_dict:
            missing_index = weights_dict[missing_weight]
            result = (missing_index, i)
            print("This is result: ", result)
            return result
        



    # compare values
    
    print("Answer is None")
    return None

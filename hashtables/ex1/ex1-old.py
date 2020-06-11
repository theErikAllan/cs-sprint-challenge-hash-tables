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

    if length == 1 and weights[0] != limit:
        return None

    if length == 2 and weights[0] + weights[1] != limit:
        return None
    elif length == 2 and weights[0] + weights[1] == limit:
        if weights[1] >= weights[0]:
            result = (1, 0)
            print("This is w2 > w1 result: ", result)
            return result
        else:
            result = (0, 1)
            print("This is w1 > w2 result: ", result)
            return result

    # use dictionaries to log index and values as key:value from 'weights'
    # First we write a for loop to go through the list of weights
    for weight in weights:
        # For each weight, we create a key:value pair in the weights dictionary where the weight is the key and the index is the value
        weights_dict[weight] = index

        # We increment the index as we go through the loop
        index += 1
    # Then, we use a for loop to go through the weights dictionary

    print("This is weights_dict: ", weights_dict)

    for weight in weights_dict:
        # For each weight in the weights dictionary, we calculate the weight we would need for the sum to equal the limit wew're given
        missing_value = limit - weight
        print("This is limit: ", limit)
        print("This is weight: ", weight)
        print("This is missing_value: ", missing_value)
        
        # Then we check to see if the missing weight we're looking for is in the weights dictionary
        if missing_value in weights_dict:
            # If we find the missing value is in the weights dictionary, we then check to see if the weight we're looking at or the missing value is greater
            if weight >= missing_value:
                result = (weights_dict[weight], weights_dict[missing_value])
                print("This is w > m result: ", result)
                return result
            else:
                result = (weights_dict[missing_value], weights_dict[weight])
                print("This is m < w result: ", result)
                return result



    # compare values
    
    print("Answer is None")
    return None

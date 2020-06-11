def has_negatives(array):
    """
    YOUR CODE HERE
    """

    dictionary = {}
    new_dict = {}

    # Your code here
    for element in array:
        if element > 0:
            dictionary[element] = True
    
    final_array = []
    for other_element in array:
        pos_element = abs(other_element)
        # print("This is pos element: ", pos_element)
        # if other_element < 0 and abs(other_element) == element:
        if other_element < 0 and dictionary[pos_element] == True:
            # print("This")
            new_dict[pos_element] = other_element
            print(f'{pos_element}: {new_dict[pos_element]}')
            final_array.append(pos_element)

    return final_array


if __name__ == "__main__":
    a = list(range(-10, 50, 1))
    # print("This is a: ", a)
    print(has_negatives(a))
    # print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

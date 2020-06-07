def has_negatives(array):
    """
    YOUR CODE HERE
    """

    dictionary = {}
    int_sum = 0

    # Your code here
    for element in array:
        if element > 0:
            for other_element in array:
                if other_element < 0 and abs(other_element) == element:
                    dictionary[element] = other_element
                    print(f'{element}: {dictionary[element]}')


                # int_sum = element + other_element
                # if int_sum == 0:
                #     dictionary[element] = other_element
                #     print("This is dictionary: ", dictionary)
        
    final_array = []
    for key in dictionary:
        final_array.append(key)
        
    # print("This is final array: ", final_array)


    return final_array


if __name__ == "__main__":
    a = list(range(-1000, 5000, 5))
    # print("This is a: ", a)
    print(has_negatives(a))
    # print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

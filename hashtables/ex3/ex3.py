def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    counts = {}
    num_of_arrays = len(arrays)
    final_array = []

    for array in arrays:
        # print("This is array: ", array)
        for element in array:
            # print("This is element: ", element)
            if element in counts:
                counts[element] += 1
                if counts[element] == num_of_arrays:
                    final_array.append(element)
                    # print("This is final_array: ", final_array)
            else:
                counts[element] = 1
            # print("This is counts: ", counts)

    return final_array


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(10, 13)) + [1, 2])
    # arrays.append(list(range(13, 16)) + [1, 2])
    # arrays.append(list(range(16, 20)) + [1, 2])

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

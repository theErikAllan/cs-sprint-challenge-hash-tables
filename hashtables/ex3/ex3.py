def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # We initialize the dictionary we'll use to count how many times a number appears
    counts = {}

    # We loop through each array
    for array in arrays:
        # And we loop through each element in each array
        for element in array:
            # We use a conditional to add the element to our dictionary or increment it by 1 if it already exists
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1

    # We initialize the output array
    result = []

    # And we use a for loop to go through the number in the dictionary to find which numbers occur as many times as there are arrays
    for element in counts:
        if counts[element] >= len(arrays):
            # For any element that appears in all arrays, we apend it to the output array
            result.append(element)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

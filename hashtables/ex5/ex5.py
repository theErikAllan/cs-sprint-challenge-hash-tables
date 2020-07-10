# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # We initialize the output array
    result = []

    # We initialize the dictionary for tracking the queries submitted
    queries_dict = {}

    # Then we add each query to the query dictionary
    for query in queries:
        queries_dict[query] = []

    # We loop through each file path we're given
    for file_path in files:
        # First we split the file path so we can point a variable to the last element in the file path, aka the name of the file
        filename = file_path.split("/")[-1]

        # We check to see if the file name exists in our queries dictionary
        if filename in queries_dict:
            # If it does, we append the file path to the output array
            result.append(file_path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

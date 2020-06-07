# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    path_dict = {}
    result = []

    for directory in files:
        for file_name in directory.split("/"):
            dictionary[directory] = file_name

        path_dict = {y: x for x, y in dictionary.items()}
        
    
    # print(path_dict)

    for query in queries:
        if query in path_dict:
            result.append(path_dict[query])
        if result == []:
            return []

            # print("This is result: ", result)
        # else:
            # return []
            # print(f'No file found under {query}')

    print("This is result before sort: ", result)
    result.sort()
    print("This is result after sort: ", result)

    return result


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    # print(finder(files, queries))

    files = []

    for i in range(100):
        files.append(f"/dir{i}/file{i}")

    for i in range(100):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    # print(files)

    queries = []

    for i in range(100):
        queries.append(f"nofile{i}")

    # queries = [
    #     "qux"
    # ]

    queries = [
        "file30",
        "file26",
        "file999",
        "file82"
    ]

    print(finder(files, queries))

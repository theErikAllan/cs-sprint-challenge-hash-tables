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
    
    # Treat value in key:value pair as an array
    # rfind - look up
    # no more than 2 for loops

    print("This is dictionary: ", dictionary)

    path_dict = {y: x for x, y in dictionary.items()}
    
    print("This is path dict: ", path_dict)

    for query in queries:
        if query in path_dict:
            result.append(path_dict[query])
            # print("This is result: ", result)
        if result == []:
            return []

            # print("This is result: ", result)
        # else:
            # return []
            # print(f'No file found under {query}')

    # print("This is result before sort: ", result)
    result.sort()
    # print("This is result after sort: ", result)

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

    # for i in range(100):
    #     files.append(f"/dir{i}/file{i}")

    # for i in range(100):
    #     files.append(f"/dir{i}/dirb{i}/file{i}")

    for i in range(10):
        files.append(f"/dir{i}/file{i}")

    for i in range(10):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    # print(files)

    queries = []

    for i in range(10):
        queries.append(f"nofile{i}")

    # queries = [
    #     "qux"
    # ]

    queries = [
        "file3",
        "file2",
        "file99",
        "file8"
    ]

    print(finder(files, queries))

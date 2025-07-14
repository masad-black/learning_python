with open("data.txt") as file:
    # * this fn will read all the file at once
    # print(file.read())

    # * this will read one line untill the space
    # print(file.readline())

    # tell some of the metadata about the file
    # print(file.encoding)
    # print(file.errors)

    # * this will tell wehther the file is in readable form or not
    # print(file.readable())

    # print(file.writable())

    # for line in file.readlines():
    #     print(line)
    print(file.readable())
    print(file.writable())

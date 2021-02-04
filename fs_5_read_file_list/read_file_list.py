def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    try:
        file_in = open(filename, 'r', closefd=True)
    except FileNotFoundError:
        print(f"The file '{filename}' was not found in the current folder.")
        return

    for file_data in file_in:
        print("- " + file_data.strip('\n'))

    print("\n\nTHANK YOU for using cats and dogs and not CHICKENS!!!!!!!!!!!")
    print("(message brought to you by students who no longer want chickens used in Rithm School video examples.)")

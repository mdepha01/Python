#in this section we will be reading and writing  to files.
ListOfLines = ["This is a first line\n", "This is a second line\n", "... This is the nth line\n"]
"""
for line in ListOfLines:
    with open("MyPythonFile.TXT", 'a') as FileObject:
        FileObject.write(line)
    """

# writing into a file using additional modes i.e r+, w+, a+
"""
with open ("MyPythonFile2.TXT", 'a+') as FileObject:
    for line in ListOfLines:
        FileObject.write(line)

    FileObject.write('I was added by a python developer\n')
    """

#In this example we are finding the location of the cursor using .tell method
with open("MyPythonFile2.TXT", 'a+') as FileObject:
    print("Cursor location {}".format(FileObject.tell()))
    # data read from a file
    data = FileObject.read()

    if (not data):
        print('Nothing was read from a file')
    else:
        print(data)

    FileObject.seek(0,0)
    print('New cursor position {}'.format(FileObject.tell()))
    data = FileObject.read()

    if (not data):
        print('nothing was read from file')
    else:
        print(data)


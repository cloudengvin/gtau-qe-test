def compare(filename1, filename2):
    with open(filename1, 'r') as file2:
        with open(filename2, 'r') as file1:
            difference = set(file1).difference(file2)
        difference.discard('\n')
    with open('diff.txt', 'w') as file_out:
        for line in difference:
            file_out.write(line)
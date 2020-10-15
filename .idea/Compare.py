with open('../dictionary.txt', 'r') as file2:
    with open('words.txt', 'r') as file1:
        difference = set(file1).difference(file2)
    difference.discard('\n')
    with open('diff.txt', 'w') as file_out:
        for line in difference:
            file_out.write(line)
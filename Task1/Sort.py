def sorting(filename):
    infile = open(filename)
    words = []
    for line in infile:
        temp = line.upper().split()
        for i in temp:
            words.append(i)
    infile.close()
    words.sort()
    outfile = open("words.txt", "w")
    for i in words:
        outfile.writelines(i)
        outfile.writelines("\n")
    outfile.close()

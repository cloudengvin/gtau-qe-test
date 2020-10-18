def countwords(filename):
    file = open(filename, "rt")
    data = file.read()
    words = data.split()

    print 'Number of words not found in dictionary.txt file :', len(words)
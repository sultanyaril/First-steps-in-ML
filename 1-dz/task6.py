def check(s, filename):
    d = {}
    unique_words = []
    s = [x.lower() for x in s.split()]
    for x in s:
        if x not in unique_words:
            unique_words.append(x)
    unique_words = sorted(unique_words);
    for w in unique_words:
        d[w] = s.count(w)
    with open(filename, "w") as out:
        for x in d:
            out.write(str(x) + ' ' + str(d[x]) + '\n')


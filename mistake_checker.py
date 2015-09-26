import os


filenames = []
for dirpath, dnames, fnames in os.walk("."):
    for f in fnames:
        if f.endswith(".tex"):
            filenames.append(dirpath +'/'+ f)


# Check for duplicate words
for filename in filenames:
    # print("Checking " + filename)
    with open(filename, 'r') as f:
        for lineno, line in enumerate(f.readlines()):
            words = line[:-1].split(' ')
            lastword = ''
            # print(words)
            for word in words:
                # print(word, lastword)
                if word is not '':
                    if word == lastword:
                        print(lineno+1, filename, word)
                    lastword = word

badlist = [
    "impedence",
    "transimpedence",
    "todo",
]

wordlist = []

# Check for mispelt words
for filename in filenames:
    # print("Checking " + filename)
    with open(filename, 'r') as f:
        for lineno, line in enumerate(f.readlines()):
            line = line.lower()
            line = line.replace('(','')
            line = line.replace(')','')
            line = line.replace(',','')
            line = line.replace('.','')
            line = line.replace('~',' ')
            line = line.replace('`','')
            # word = word.replace('\\','')
            line = line.replace('}','')
            line = line.replace('{','')
            words = line[:-1].split(' ')
            for word in words:
                for bword in badlist:
                    if word.find(bword) != -1:
                        print("Found occurrence of " + bword + " on line " + str(lineno) + " of " + filename)
                # if len(word) > 0 and word[0] in "0123456789":
                #     print("Found occurrence of " + word[0] + " on line " + str(lineno) + " of " + filename)
                if word.find('\cite') == -1 and len(word) > 0:
                    if word[0] not in "0123456789\\%+=><@[]/$&!^":
                        if word.find("^") == -1 and word.find('\\') == -1:
                          if word not in wordlist:
                            wordlist.append(word)

wordlist.sort()

with open('wordlist.txt', 'w') as f:
    for word in wordlist:
        f.write(word+"\n")
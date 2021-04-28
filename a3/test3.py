def compute_tweets(name1, name2):
    with open(name1, "r", encoding="utf-8") as tweetfile, open(name2, "r", encoding="utf-8") as keyfile:
        keylist = []
        for line in keyfile:
            line = line.strip()
            y = line.split(",")
            element = ','.join(y)
            keylist.append(element)
        list1 = []
        list2 = []
        for x in keylist:
            x = x.split(",")
            list1.append(x[0])
            list2.append(x[1])
        punctuation = '''!()-[]{};:' "\,<>./?@#$%^&*_~'''
        pkeywords = 0
        mkeywords = 0
        ckeywords = 0
        ekeywords = 0

        for line in tweetfile:
            line = line.split()
            line2 = [x[1:-1] if x[0] == '[' else x[:-1] if x[-1] == ']' else x for x in line]
            line = [''.join(c for c in s if c not in punctuation) for s in line[5:]]
            line = [s.lower() for s in line if s]
            print(line)
            print(line2)
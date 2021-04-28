def latcheck(x):
    return 49.189787 >= x >= 24.660845


def pcheck(x):
    return -115.236428 > x >= -125.242264


def mcheck(x):
    return -101.998892 > x >= -115.236428


def ccheck(x):
    return -87.518395 > x >= -101.998892


def echeck(x):
    return -67.444574 >= x >= -87.518395


def happiness_calculate(x, y):
    return round((x / float(y)), 1) if y != 0 else 0


def compute_tweets(name1, name2):
    try:
        with open(name1, "r", encoding="utf-8") as tweetfile, open(name2, "r", encoding="utf-8") as keyfile:
            # initialize keylist as a list
            keylist = []

            for line in keyfile:
                line = line.strip()
                y = line.split(",")
                element = ','.join(y)
                keylist.append(element)

            # initialize list for each word and happiness value in the keylist
            list1 = []
            list2 = []

            for x in keylist:
                x = x.split(",")
                list1.append(x[0])
                list2.append(x[1])

            punctuation = '''!()-[]{};:' "\,<>./?@#$%^&*_~'''
            # initialize counters for happiness value, number of keyword tweets, and number of tweets in each region
            pacific = mountain = central = eastern = 0
            pkeywords = mkeywords = ckeywords = ekeywords = 0
            pcount_of_tweets = mcount_of_tweets = ccount_of_tweets = ecount_of_tweets = 0

            for line in tweetfile:
                line = line.split()
                # delete punctuation from beginning and end of each element in the list
                line2 = [x[1:-1] if x[0] == '[' else x[:-1] if x[-1] == ']' else x for x in line]
                line = [''.join(c for c in s.strip(punctuation)) for s in line[5:]]
                line = [s.lower() for s in line if s]
                lat = float(line2[0])
                long = float(line2[1])

                # check lat and long for each tweet and increment keywords number for each region
                if latcheck(lat):
                    if echeck(long):
                        ecount_of_tweets = ecount_of_tweets + 1
                        echecker = any(x in line for x in list1)
                        if echecker is True:
                            ekeywords = ekeywords + 1
                    elif ccheck(long):
                        ccount_of_tweets = ccount_of_tweets + 1
                        cchecker = any(x in line for x in list1)
                        if cchecker is True:
                            ckeywords = ckeywords + 1
                    elif mcheck(long):
                        mcount_of_tweets = mcount_of_tweets + 1
                        mchecker = any(x in line for x in list1)
                        if mchecker is True:
                            mkeywords = mkeywords + 1
                    elif pcheck(long):
                        pcount_of_tweets = pcount_of_tweets + 1
                        pchecker = any(x in line for x in list1)
                        if pchecker is True:
                            pkeywords = pkeywords + 1

                for word in line:
                    if word in list1:
                        # check lat and long for each tweet and assign them to a counter
                        if latcheck(lat):
                            if echeck(long):
                                eastern = eastern + int(list2[list1.index(word)])

                            elif ccheck(long):
                                central = central + int(list2[list1.index(word)])

                            elif mcheck(long):
                                mountain = mountain + int(list2[list1.index(word)])

                            elif pcheck(long):
                                pacific = pacific + int(list2[list1.index(word)])

            # calculate happiness values, making sure not to divide by 0
            phappiness = happiness_calculate(pacific, pkeywords)
            mhappiness = happiness_calculate(mountain, mkeywords)
            chappiness = happiness_calculate(central, ckeywords)
            ehappiness = happiness_calculate(eastern, ekeywords)
            print(eastern)
            average = (phappiness, mhappiness, chappiness, ehappiness)
            count_of_keyword_tweets = (pkeywords, mkeywords, ckeywords, ekeywords)
            count_of_tweets = (pcount_of_tweets, mcount_of_tweets, ccount_of_tweets, ecount_of_tweets)
            return list(tuple(zip(average, count_of_keyword_tweets, count_of_tweets)))

    # error handling
    except:
        emptylist = []
        return emptylist

from test2 import compute_tweets

file1 = "tweetstest.txt"
file2 = "tweetskey.txt"
try:
    answer = compute_tweets(file1, file2)

    print("The average happiness value, number of keyword tweets, and number of tweets, respectively, in the pacific "
          "region is:{}".format(answer[0]))
    print("The average happiness value, number of keyword tweets, and number of tweets, respectively, in the mountain "
          "region is:{}".format(answer[1]))
    print("The average happiness value, number of keyword tweets, and number of tweets, respectively, in the central "
          "region is:{}".format(answer[2]))
    print("The average happiness value, number of keyword tweets, and number of tweets, respectively, in the eastern "
          "region is:{}".format(answer[3]))
except:
    print("Wrong file or file path")

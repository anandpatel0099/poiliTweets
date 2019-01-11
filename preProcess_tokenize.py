#import regex
import re
import csv
import twitter, sys, json
import preprocessor as p

#start process_tweet
def processTweet(tweet):
    # process the tweets
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    yourstring = tweet.encode('ascii', 'ignore').decode('ascii')
    new_tweet = p.clean(yourstring)
    str= p.tokenize(new_tweet)
    #return str
    with open('CNG_test_main.txt', 'a') as createFile:
        createFile.write((str)+ '\n')
    #for raw_tweet in str:
    #createFile.write(json.dumps(raw_tweet) + '\n')
    createFile.close()
#end
def rest_query_ex3():
    #Read the tweets one by one and process it
    fp = open('CNG_test.txt', 'r')
    line = fp.readline()


    while line:
        processedTweet = processTweet(line)
        print processedTweet
        line = fp.readline()

#end loop
    fp.close()

def main():

    print "\n\n\n************ rest_query_ex1() ****************\n"
    rest_query_ex3()

pass

if __name__ == '__main__':
    main()
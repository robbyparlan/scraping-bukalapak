
#import regex
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd
import csv
 
factory = StemmerFactory()
stemmer = factory.create_stemmer()
 
#start process_tweet
def processTweet(tweet):
    # process the tweets
 
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub("((www\.[^\s]+)|(https?://[^\s]+))","URL",tweet)
    #Convert @username to AT_USER
    tweet = re.sub("@[^\s]+","AT_USER",tweet)
    #Remove additional white spaces
    tweet = re.sub("[\s]+", " ", tweet)
    #Replace #word with word
    tweet = re.sub(r"#([^\s]+)", r"\1", tweet)
    #trim
    tweet = tweet.strip('\'"')
    #stemming
    tweet = stemmer.stem(tweet)
    return tweet
#end
 
 
#Read the tweets one by one and process it
fp = open("ambil.csv", "r+", encoding="ascii", errors="ignore")
line = fp.readline()
while line:
    processedTweet = processTweet(line)
    print (processedTweet)
    line = fp.readline()
#end loop
fp.close()
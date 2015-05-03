import sys
import csv

def seg_file(dfile):

    inpTweets = csv.reader(open(dfile, 'rb'), delimiter=',', quotechar='|')
    pfile = open(dfile+"_pos", "a")
    nfile = open(dfile+"_neg", "a")
    nufile = open(dfile+"_nue", "a")
    irfile = open(dfile+"_irr", "a")
    for row in inpTweets:
        sentiment = row[0]
        tweet = row[1].strip()
        if sentiment == 'positive':
            pfile.write(tweet)
            pfile.write('\n')
        elif sentiment == 'negative':
            nfile.write(tweet)
            nfile.write('\n')
        elif sentiment == 'neutral':
            nufile.write(tweet)
            nufile.write('\n')
        else :
            irfile.write(tweet)
            irfile.write('\n')


if __name__ == '__main__':

    seg_file(sys.argv[1])


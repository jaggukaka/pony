import json
import pandas as p

tweets_data_path = 'tweets.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print len(tweets_data)

tweets = p.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

with open("tweetscsv.csv", "a") as myfile:
	myfile.write('text')
	myfile.write('\n')
	for vals in tweets['text']:
		myfile.write(vals.encode('utf8'))
		myfile.write('\n')
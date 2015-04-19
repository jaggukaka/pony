from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1131382249-vpxkHlvFKeB32q6TZIqgkSV6maP8uue5XidbB1x"
access_token_secret = "IfYQGPOCF8iBo1LsCyZin1wi7dbLKO5J8UYJf9qUHhflq"
consumer_key = "cnimc04rhteJOeRTddXY15YDR"
consumer_secret = "j9WDy5Gb2BdWcVHO9Lg5kAWQhr7NTbSKLnQVbi6O6SrUhzVKTA"



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self):
        self.count = 0

    
    def on_data(self, data):

        with open("tweets.txt", "a") as myfile:
            myfile.write(data)
            myfile.write('\n\n')
        
        with open("count.txt", "w") as cfile:
            self.count += 1
            cfile.write(str(self.count))

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#makeinindia'])

import tweepy
import json
import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from io import open

#Variables that contains the user credentials to access Twitter API 
access_token = 'ZM0BcATbMQbFlgNffhjhslN1m'
access_token_secret = 'ke4ibybicbfed50QWJditlyjzWkFjsBeSZ24vljefcp5KrxSI3' 
consumer_key = '1190665689243234305-Bu492RHdEu7YWjHCpmTyXNinSqMMON'
consumer_secret = 'yG8uyVbUt8SsoSdF6RHjmjM2KWshislrlyHYHmlSQjECO'

class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API as well as writing them onto a text i
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(access_token, access_token_secret)
        auth.set_access_token(consumer_key, consumer_secret)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        #stream.filter(locations = [-6.03,49.96,1.79,58.71], languages=['en'])
        stream.filter(track = hash_tag_list, languages=['en'])

        
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self, data):
        try:
            with open(self.fetched_tweets_filename, 'a') as tf:
                writer = csv.writer(tf)
                tweet = json.loads(data)
                if "extended_tweet" in tweet:
                    name = tweet['user']['name'] 
                    text = tweet['extended_tweet']['full_text']
                    print(text)
                    for keyword in domestic_violence:
                        if keyword in text:
                            writer.writerow([name, text, "domestic violence"])                           
                    for keyword in sexual_harassment:
                        if keyword in text:
                            writer.writerow([name, text, "sexual harassment"])
                    for keyword in unequal_pay:
                        if keyword in text: 
                            writer.writerow([name, text, "unequal pay"]) 
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    domestic_violence = ["#SurvivorSpeaks", "#domesticviolence", "#domesticviolenceawareness", "#AbuseHasNoGender", "#traumabonding", "#domesticabuse", "#emotionalabuse", "#hounourkillings", "#psychologicalabuse", "#childabuse",
                         "#religiousabuse", "#femalemutilation", "#fgm", "#DV", "#abused", "#narcissisticabuse", "#narcissism" "#domesticviolencesurvivor", "#childmarriage"]
    sexual_harassment = ["#MeToo", "#TimesUp", "#WhyIDidntReport", "#violenceagainstwomen", "#rapesurvivor", '#rapeculture', "#sexualabuse", "#sexualassault", "#metoomovement", "#sexabuse", "#HimToo", "#rapesurvivor",
                         "#rapevictim", "#sexualharassment", "#nomeansnno"]
    unequal_pay = ["#EqualPay", "#equalpay", "#PayGap", "#genderpaygap", "#GenderPayGap", "#BlackWomensEqualPay", "#PaycheckFairness", "#PayEquality", "#sexpaygap", "#equalpayday"]
    hash_tag_list = ["#SurvivorSpeaks", "#domesticviolence", "#domesticviolenceawareness", "#AbuseHasNoGender", "#traumabonding", "#domesticabuse", "#emotionalabuse", "#hounourkillings", "#psychologicalabuse", "#childabuse",
                     "#religiousabuse", "#femalemutilation", "#fgm", "#DV", "#abused", "#narcissisticabuse", "#narcissism" "#domesticviolencesurvivor", "#childmarriage", "#MeToo", "#TimesUp", "#WhyIDidntReport", "#violenceagainstwomen",
                     "#rapesurvivor", '#rapeculture', "#sexualabuse", "#sexualassault", "#metoomovement", "#sexabuse", "#HimToo", "#rapesurvivor", "#rapevictim", "#sexualharassment", "#nomeansnno", "#EqualPay", "#equalpay", "#PayGap",
                     "#genderpaygap", "#GenderPayGap", "#BlackWomensEqualPay", "#PaycheckFairness", "#PayEquality", "#sexpaygap", "#equalpayday"]
    fetched_tweets_filename = "tweets_collected.csv"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

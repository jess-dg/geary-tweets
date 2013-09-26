import json
from database import *

tweets = open('tweets.txt').readlines()

Base.metadata.create_all(engine)

for tweet_json in tweets:
	#take pieces of the string and make it a python object
#	print "About to decode line: %s" % tweet_json
	tweet_fields = json.loads(tweet_json)
	current_tweet = Tweet()
	current_tweet.tweet_id = tweet_fields["id"]
	current_tweet.tweet_created_at = to_datetime(tweet_fields["created_at"])
	current_tweet.tweet_text = tweet_fields["text"]

	if tweet_fields["geo"]:
		current_tweet.latitude = tweet_fields["geo"]["coordinates"][0]
		current_tweet.longitude = tweet_fields["geo"]["coordinates"][1]

	session.add(current_tweet)
	session.commit()

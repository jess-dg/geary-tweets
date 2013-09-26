from flask import Flask, render_template
from database import *
from sqlalchemy import asc
from json import *

app = Flask(__name__)

@app.route('/')
def index():
	tweets = session.query(Tweet).filter((Tweet.latitude.between(37.77713,37.78913)),(Tweet.longitude.between(-122.51030,-122.40181))).order_by(Tweet.longitude.asc())
	return render_template('tweet_page.html', tweets=tweets)

@app.route('/generate')
def create_json():
	tweets = session.query(Tweet).filter((Tweet.latitude.between(37.77713,37.78913)),(Tweet.longitude.between(-122.51030,-122.40181))).order_by(Tweet.longitude.asc())
	tweet_dicts = []
	for tweet in tweets:
		tweet_dicts.append({'title': tweet.tweet_text,
							'latLong': [tweet.latitude, tweet.longitude], 
							'longitude': [tweet.longitude], 
							'latitude': [tweet.latitude]})

	return dumps(tweet_dicts)

@app.route('/landmarks')
def create_json():
	landmarks = session.query(Landmark)
	landmark_dicts = []
	for landmark in landmarks:
		landmark_dicts.append({'name': [landmark.name], 
								'sideOfStreet': [landmark.side_of_street], 
								'latLong': [landmark.latitude, landmark.longitude], 
								'longitude': [landmark.longitude], 
								'latitude': [landmark.latitude]})

	return dumps(landmark_dicts)

@app.route('/pretty')
def new_map():
	tweets = session.query(Tweet).filter((Tweet.latitude.between(37.77713,37.78913)),(Tweet.longitude.between(-122.51030,-122.40181))).order_by(Tweet.longitude.asc())
	return render_template('pretty_tweet_page.html', tweets=tweets)	

if __name__ == '__main__':
    app.run(debug=True)




#query lat at 1 post = 37.78913, long = -122.40181
#lat at 1 o'farrell = 37.78693, long = -122.40448

#lat at anza 37.77713, long -122.51013
# at seal rock dr = 37.78092, -122.51030


#where latitude between  37.77713 and 37.78913
#longitude between -122.40181 and -122.51030
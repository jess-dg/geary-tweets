from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, distinct, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from email.utils import parsedate_tz
from datetime import datetime, timedelta

engine = create_engine('sqlite:////Users/jessicadegeorge/desktop/projects/geary_tweets/tweet_db.sqlite', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Tweet(Base):
	__tablename__ = "Tweets"
	tweet_id = Column(Integer, primary_key=True)
	tweet_created_at = Column(DateTime)
	tweet_text = Column(String)
	latitude = Column(Float, index=True)
	longitude = Column(Float, index=True)
	load_date = Column(DateTime, default=datetime.now)


def to_datetime(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])

class Landmark(Base):
	__tablename__ = "Landmarks"
	landmark_id = Column(Integer, primary_key=True)
	name = Column(String)
	latitude = Column(Float, index=True)
	longitude = Column(Float, index=True)
	side_of_street = Column(String) #nsew
	description = Column(String)
	image_filepath = Column(String)
	load_date = Column(DateTime, default=datetime.now)

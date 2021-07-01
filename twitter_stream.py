# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:44:52 2021

@author: Admin
"""
#authentication class
from tweepy import OAuthHandler
#a class from tweepy that will help us listen to the tweets
from tweepy.streaming import StreamListener
from tweepy import Stream
import twitter_credentials
import os


#this class will print the data we listen to and will be inherit the stream listener class
#we can overrde methods of streamlistener class
class OutputListener(StreamListener):
    """
    This is basic listener that just prints received tweets to outputlistener
    """
    #create constructor with parameter where i want to store my filename
    def __init__(self,fetched_tweet_filename):
        self.fetched_tweet_filename=fetched_tweet_filename
    
    #this function is used for data that we receive or that we listen to
    def on_data(self,data):
        try:
            print(data)
            #a means append because we want to append our tweets to a file
            #t is the file object
            with open(self.fetched_tweet_filename,'a') as t:
                t.write(data)
                return True
        except BaseException as st:
            print("Error in data:%s"%str(st))
        return True
    # prints the status of our request
    def on_error(self,status):
        print(status)
        #create object in the main function
        #function will run automatically
        
#we will define a class that will stream our tweets and maintain it for us
#wait_on_rate_limit_notify ==where we want to store our tweets ,in which file
#hash_tag_list== list to filter by
class Streamer():
    """
    Class for processing and streaming live tweets
    """
    #This handles our authentication and connection to twitter streaming api
    def stream_tweets(self,fetched_tweet_filename,hash_tag_list):
        listener=OutputListener(fetched_tweet_filename)
        auth=OAuthHandler(twitter_credentials.API_KEY,twitter_credentials.API_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
        #listener object is used to encounter the data and see what to do if i encounter an error
        #stream is the object of Stream class
        stream=Stream(auth,listener)
        #if we stream here we'll get random tweets, we want tweets that are particular
        #filter uses specific data(list) or hashtags to filter our data
        stream.filter(track=hash_tag_list)
        
    
if __name__=="__main__":
    hash_tag_list=['code','datascience','machine learning']
    path=os.path.join('stream_tweets/')
    os.makedirs(path,exist_ok=True)
    fetched_tweet_filename=path+"tweets.json"
    streamer=Streamer()
    streamer.stream_tweets(fetched_tweet_filename,hash_tag_list)
    
    
   
       
    
    

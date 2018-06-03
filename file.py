from datetime import datetime, timedelta
from dateutil.parser import parse
from json import loads
from os import listdir
from os.path import join
from re import match

FILE_START = "Grailbird.data.tweets_(\d*)_(\d*)"

def get_all_files(export_path):
    return [join(export_path, file) for file in listdir(export_path)]

def read_file(filename):
    json = None
    
    try:
        with open(filename) as file:
            file_data = file.read()
            
            if match(FILE_START, file_data):
                separator_index = file_data.find("=") + 1
                json_data = file_data[separator_index:]
                json = loads(json_data)
    except:
        print("Could not open file " + filename)
        
    return json
    
def parse_tweet(tweet_json):
    date = tweet_json["created_at"]
    id = str(tweet_json["id"])
    return {"date": parse(date).replace(tzinfo=None), "id": id} 
    
def parse_twitter_data(json):
    return [parse_tweet(tweet_json) for tweet_json in json]
    
def filter_new_tweets(tweets, number_months):
    today = datetime.now()
    time_delta = timedelta(days = (number_months * 30))
    print(tweets)
    return [tweet for tweet in tweets if today - tweet["date"] > time_delta]
    
def get_tweets(export_path, number_months):
    files = get_all_files(export_path)
    jsons = [read_file(file) for file in files]
    tweets_list = [parse_twitter_data(json) for json in jsons]
    tweets = [tweet for tweets in tweets_list for tweet in tweets]
    return filter_new_tweets(tweets, number_months)

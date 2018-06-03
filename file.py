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
	
def parse_twitter_data(json):
	tweets = []
	
	if json:
		for tweet in json:
			date = tweet["created_at"]
			id = str(tweet["id"])
			tweets.append({"date": parse(date).replace(tzinfo=None), "id": id})
		
	return tweets
	
def filter_new_tweets(tweets, number_months):
	today = datetime.now()
	time_delta = timedelta(days = (number_months * 30))
	return [tweet for tweet in tweets if today - tweet["date"] > time_delta]
	
def get_tweets(export_path, number_months):
	files = get_all_files(export_path)
	tweets = []
	
	for file in files:
		json = read_file(file)
		tweets += parse_twitter_data(json)
	
	return filter_new_tweets(tweets, number_months)

from configparser import RawConfigParser
from dao import delete_tweet
from file import get_tweets
from time import sleep

CONFIG_FILE = "./config"

def read_config():
	config = RawConfigParser()
	config.read(CONFIG_FILE)
	return config
	
def delete_tweets(tweets, token, cookie, account):	
	for tweet in tweets:
		sleep(1)

		if delete_tweet(token, tweet["id"], cookie, account):
			print("Successfully deleted " + str(tweet["date"]))
		else:
			print("Failed to delete " + str(tweet["date"]))

if __name__ == "__main__":
	config = read_config()
	
	export_path = config["settings"]["export_path"]
	months_to_keep = int(config["settings"]["months_to_keep"])
	token = config["twitter"]["token"]
	cookie = config["twitter"]["cookie"]
	account = config["twitter"]["account"]
	
	tweets = get_tweets(export_path, months_to_keep)
	delete_tweets(tweets, token, cookie, account)
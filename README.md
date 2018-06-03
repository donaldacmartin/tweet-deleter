# Tweet Deleter

## Purpose

The standard [Twitter API](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-destroy-id) will only allow the deletion of up to 3,000 previous tweets: it cannot go further back. The purpose of this tool is to go back to the beginning of your account's history, and delete going forward (up to one year ago is the default).

## Requirements

- Python 3.6 or greater
- Exported archive of tweets (from your [account settings page](https://twitter.com/settings/account))

## Usage

The config file needs to be updated to include some data from your web browser:

- **account** = your Twitter handle
- **token** = while browsing the website, open developer tools, look at params and steal the authenticity token
- **cookie** = as above, open developer tools and steal your cookie string (all of it)
- **export_path** = the path to the tweets folder in your exported archive, under data/js

After that, simply run "python twitter.py"

## Known Limitations

- The script currently does not support paths with non-ASCII characters. This may change in the future.
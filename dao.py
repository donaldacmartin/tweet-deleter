from http import HTTPStatus 
from requests import post
from urllib.parse import urlencode

TWITTER_URL = "https://twitter.com/i/tweet/destroy"

def create_post_form(token, id):
    params = {"_method": "DELETE", "authenticity_token": token, "id":id}
    return urlencode(params)

def create_headers(cookie, twitter_account):
    headers = {}
    
    headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers["Cookie"] = cookie
    headers["Referer"] = "https://twitter.com/" + twitter_account
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["X-Twitter-Active-User"] = "yes"
    
    return headers
    
def delete_tweet(authenticity_token, tweet_id, cookie, twitter_account):
    try:
        post_form = create_post_form(authenticity_token, tweet_id)
        headers = create_headers(cookie, twitter_account)
        status = post(TWITTER_URL, data=post_form, headers=headers)
        return status.status_code == HTTPStatus.OK
    except:
        print("Error while calling Twitter")
        return False

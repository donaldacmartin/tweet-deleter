from http.HTTPStatus import OK
from requests import post
from urllib.parse import urlencode

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
	
def delete_tweet(url, authenticity_token, id):
	post_form = create_post_form(authenticity_token, id)
	headers = create_headers()
	status = post(url, data=post_form, headers=headers)
	return status.status_code == OK

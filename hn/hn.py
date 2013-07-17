#this script pushes urls of hackernews stories to the sailthru content api
import requests
import json
from sailthru.sailthru_client import SailthruClient
from BeautifulSoup import BeautifulSoup

with open('settings.json') as json_data:
    data = json.load(json_data)
    api_key = data["api_key"]
    api_secret = data["api_secret"]
sailthru_client = SailthruClient(api_key, api_secret, "http://api.sailthru.com")

feed_50 = "http://feeds.feedburner.com/hacker-news-feed-50?format=xml"
feed_100 = "http://feeds.feedburner.com/hacker-news-feed-100?fmt=xml"
feed_200 = "http://feeds.feedburner.com/hacker-news-feed-200?format=xml"

def pull_and_push(url,points):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for item in soup.findAll('guid'):
        data={"url": item.text, "spider":1, "vars":{"points":points}}
        response = sailthru_client.api_post("content",data)
        print response.get_body()
pull_and_push(feed_50,50)
pull_and_push(feed_100,100)
pull_and_push(feed_200,200)

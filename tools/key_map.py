#example of key mapping 

a = raw_input("Enter a env: ")

env_urls = {
    "qa": "http://api.sailthru-qa.com",
    "prod": "http://api.sailthru.com",
    "dev": "http://api.sailthru-dev.com",
}

env_url = env_urls[a]

print (env_url)



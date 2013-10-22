import unirest

destination =  "http://httpbin.org/post"
num = 500

def callback(response):
  print response.code
  print response.headers
  print response.body
  print response.raw_body

def run(num, destination):
    for n in range(0, num):
        thread = unirest.post(destination, { "Accept": "application/json" }, { "parameter": 23, "foo": "bar" }, callback)

run(num, destination)

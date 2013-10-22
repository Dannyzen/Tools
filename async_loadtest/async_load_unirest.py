import unirest

destination =  "http://httpbin.org/post"
num = 500

def callback(response):
  response.code # The HTTP status code
  print response.code
  response.headers # The HTTP headers
  print response.headers
  response.body # The parsed response
  print response.body
  response.raw_body # The unparsed response
  print response.raw_body

def run(num, destination):
    for n in range(0, num):
        thread = unirest.post(destination, { "Accept": "application/json" }, { "parameter": 23, "foo": "bar" }, callback)
        print thread
run(num, destination)

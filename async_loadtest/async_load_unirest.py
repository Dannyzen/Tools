import unirest

def callback(response):
  response.code # The HTTP status code
  print response.code
  response.headers # The HTTP headers
  print response.headers
  response.body # The parsed response
  print response.body
  response.raw_body # The unparsed response
  print response.raw_body

x = 0
while x < 500:
    thread = unirest.post("http://httpbin.org/post", { "Accept": "application/json" }, { "parameter": 23, "foo": "bar" }, callback)
    print thread
    x = x+1

# Importing the requests library
import requests

# URL to send a request to
url = "http://example.com"

# Sending a GET request
response = requests.get(url)

# Print the response text
print(response.text)

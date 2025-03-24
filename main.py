import requests

api_key = "81d713aa3e504a63b7f7e7f525899127"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-02-24&sort"
       "By=publishedAt&apiKey=81d713aa3e504a63b7f7e7f525899127")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article titles and description
for article in content["articles"]:
       print(article["title"])
       print(article["description"])
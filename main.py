import requests
from send_email import send_email

topic = "tesla"

api_key = "81d713aa3e504a63b7f7e7f525899127"
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=81d713aa3e504a63b7f7e7f525899127&"
       "language=pt")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news\n\n"  # Add subject header once
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += article["title"] + "\n" \
                + str(article["description"]) + "\n" \
                + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
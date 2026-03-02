import requests

API_KEY ="d3e24d6b326a460984c70c6a51799a0f"

topic = input("Enter a topic: ")
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(url)

data = response.json()

if data["status"] == "ok":
    for article in data["articles"][:5]:
        print(article["title"])
        print(article["url"])
        print("-"*50)
else:
    print("Error: ", data["message"])

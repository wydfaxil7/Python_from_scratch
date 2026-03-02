import requests
import win32com.client
from datetime import date, timedelta

today = date.today()
three_days_ago = today - timedelta(days=3)

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Voice = speaker.GetVoices().Item(0)  # choose different voice

topic = input("Enter a topic you want news about: ").strip()

API_KEY = "d3e24d6b326a460984c70c6a51799a0f"

url = f"https://newsapi.org/v2/everything?q={topic}&from={three_days_ago}&sortBy=publishedAt&language=en&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

# check if news is available
articles = data.get("articles", [])
if not articles:
    print(f"No news found for '{topic}'.")
    speaker.Speak(f"No news found for '{topic}'.")
else:
    print(f"\nTop {min(5, len(articles))} news about '{topic}'")

    for i, article in enumerate(articles[:5], start=1):
        title = article['title']
        source = article['source']['name']
        text_to_speak = f"News {i}: {title} from {source}"

        print(f"{i}. {title}")
        print(f"Source: {source}")
        print(f"URL: {article['url']}")
        print("-" * 50)

        speaker.Speak(text_to_speak)
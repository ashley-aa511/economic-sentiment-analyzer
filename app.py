from newspaper import Article
from textblob import TextBlob
import pandas as pd
import os

# Make sure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

# List of ECONOMIC article URLs (not full pages—actual article links)
urls = [
    "https://blogs.worldbank.org/en/opendata/artificial-intelligence-in-the-kyrgyz-republic--a-silent-transfo",
    "https://www.imf.org/en/Countries/KEN",
    "https://www.imf.org/en/News/Articles/2025/04/22/tr-04222025-weo-press-briefing",
    "https://www.worldbank.org/en/country/kenya/overview",
    "https://www.economicsobservatory.com/kenyas-economy-how-is-the-government-tackling-the-big-challenges"
    ]

headlines = []
sentiments = []

print("🧠 Analyzing Economic Headlines...\n")

for url in urls:
    try:
        article = Article(url)
        article.download()
        article.parse()

        title = article.title
        blob = TextBlob(title)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        headlines.append(title)
        sentiments.append(sentiment)

        print(f"✓ {title} → {sentiment}")

    except Exception as e:
        print(f"⚠️ Failed to process {url}: {e}")

# Save to CSV
df = pd.DataFrame({
    'Headline': headlines,
    'Sentiment': sentiments
})
df.to_csv("data/headline_sentiment.csv", index=False)

print("\n✅ Results saved in data/headline_sentiment.csv")

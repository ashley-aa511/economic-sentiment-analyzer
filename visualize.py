import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load CSV
df = pd.read_csv("data/headline_sentiment.csv")  # Change this to your actual filename
print(df.head())
print(df.columns)

# Countplot of Sentiments
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.countplot(x='Sentiment', hue='Sentiment', data=df, palette='Set2', legend=False)
plt.title('Sentiment Distribution of Economic Headlines')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.savefig('images/sentiment_bar_chart.png')
plt.show()

# WordCloud of Titles
text = ' '.join(df['Headline'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Economic Headlines')
plt.savefig('images/wordcloud_headlines.png')
plt.show()

# Pie Chart
sentiment_counts = df['Sentiment'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set2"))
plt.title('Sentiment Share')
plt.savefig('images/sentiment_pie_chart.png')
plt.show()

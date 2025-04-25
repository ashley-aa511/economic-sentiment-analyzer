# 🧠 AI-Powered Economic Sentiment Analyzer

A Python tool that scrapes real-world economic news articles and uses Natural Language Processing (NLP) to analyze the sentiment behind them. Built during my #100DaysOfCode journey to explore the intersection of AI and Economics.

---

## 🔍 What It Does

- Scrapes news articles from sources like [Nation Africa](https://nation.africa) and [Business Daily](https://www.businessdailyafrica.com)
- Analyzes sentiment (Positive / Neutral / Negative) using `TextBlob`
- Outputs results into a clean `.csv` file for further analysis or visualization
- Generates visualizations (bar chart, pie chart, word cloud)

---

## ⚙️ Tech Stack

- **Python 3**  
- `newspaper3k` – Article scraping  
- `TextBlob` – Sentiment analysis  
- `pandas` – Data manipulation  
- `matplotlib`, `seaborn`, `wordcloud` – Visualization  
- `lxml_html_clean` – Clean HTML parsing  

---

## 📁 Project Structure

```text
econ_sentiment_analyzer/
│
├── data/
│   └── headline_sentiment.csv          # Scraped headlines + sentiment
│
├── images/
│   ├── sentiment_bar_chart.png         # Bar chart of sentiment
│   ├── wordcloud_headlines.png         # Word cloud of headlines
│   └── sentiment_pie_chart.png         # Pie chart of sentiment share
│
├── app.py                              # Scrapes & analyzes headlines
├── visualize.py                        # Generates and saves charts
└── README.md                           # This file

🌍 SDG Problem Addressed
By surfacing the tone of economic reporting, this project supports:

SDG 1: No Poverty
Early detection of economic stressors to protect vulnerable communities.

SDG 8: Decent Work and Economic Growth
Insight into investor and public confidence for informed policymaking.

SDG 10: Reduced Inequalities
Highlighting differential impacts of economic events on various groups.

SDG 16: Peace, Justice and Strong Institutions
Tracking sentiment on governance-related articles to promote transparency.

SDG 17: Partnerships for the Goals
Open-source collaboration to expand and adapt the tool globally.

🚀 How to Run It
1. Clone the repo
git clone https://github.com/your-username/economic-sentiment-analyzer.git
cd economic-sentiment-analyzer

2. Install dependencies
pip install -r requirements.txt

3. Scrape & analyze
python app.py
This will update data/headline_sentiment.csv.

4. Generate visualizations
python visualize.py
Charts will be saved in the images/ folder.

📊 Sample Output
data/headline_sentiment.csv

headline	sentiment
Kenya shilling recovers slightly against Dollar	Positive
IMF to send review mission as Kenya eyes new loan	Neutral
Inflation falls to 5.7 percent in March	Positive
Nairobi Stock Exchange hits 5-year low	Negative
Visuals

🌟 Contributing
PRs, issues, and suggestions are more than welcome! Feel free to fork the repo and submit improvements.

📝 License
This project is licensed under the MIT License.

🐦 Stay Connected
Follow my #100DaysOfCode journey on Twitter or connect on LinkedIn.
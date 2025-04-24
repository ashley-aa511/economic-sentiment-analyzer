# AI-Powered Economic Sentiment Analyzer

A Python tool that scrapes real-world economic news articles and uses Natural Language Processing (NLP) to analyze the sentiment behind them. Built during my #100DaysOfCode journey to explore the intersection of AI and Economics.

---

## 🔍 What It Does

- Scrapes news articles from sources like [Nation Africa](https://nation.africa) and [Business Daily](https://www.businessdailyafrica.com)
- Analyzes sentiment (Positive / Neutral / Negative) using `TextBlob`
- Outputs results into a clean `.csv` file for further analysis or visualization

---

## ⚙️ Tech Stack

- **Python 3**
- `newspaper3k` – Article scraping
- `TextBlob` – Sentiment analysis
- `Pandas` – Data manipulation
- `lxml_html_clean` – Clean HTML parsing

---

## 🧠 Why This Matters

### Aligning with the UN Sustainable Development Goals (SDGs):

- **SDG 1: No Poverty**  
  Early detection of economic stressors can help vulnerable communities prepare or respond effectively.

- **SDG 8: Decent Work and Economic Growth**  
  Insights into media sentiment can reflect public and investor confidence, crucial for informed business and policy decisions.

- **SDG 10: Reduced Inequalities**  
  Localized economic sentiment can highlight how different groups are impacted by national and global economic events.

- **SDG 16: Peace, Justice and Strong Institutions**  
  Sentiment analysis on governance-related articles offers a lens into institutional trust and transparency.

- **SDG 17: Partnerships for the Goals**  
  This project is open-source and invites collaboration from anyone passionate about AI, economics, or development.

---

## 🚀 How to Run It

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/economic-sentiment-analyzer.git
cd economic-sentiment-analyzer

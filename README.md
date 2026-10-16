# BCG-X-GenAI-Job-Simulation-on-Forage
<div align="center">

# 📈 AI Financial Chatbot: BCG X GenAI Job Simulation

**From raw SEC 10-K filings ➜ Python analysis ➜ a working finance chatbot**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/status-completed-brightgreen)
![Forage](https://img.shields.io/badge/Forage-BCG%20X%20Certified-1A7F5A)

*Built by **Vaibhav Sable** · October 2026*

</div>

---

## ⚡ TL;DR

| | |
|---|---|
| 🎯 **Mission** | Analyse Microsoft, Tesla & Apple financials, then build a chatbot that answers questions about them |
| 📊 **Data** | Revenue, Net Income, Total Assets, Total Liabilities, Operating Cash Flow (FY2023–FY2025) |
| 🛠️ **Stack** | Python · pandas · matplotlib · Jupyter |
| 🤖 **Chatbot** | Rule-based, 5 query types, company + year detection, graceful error handling |
| 🏆 | Completed both tasks of the **BCG X GenAI Job Simulation** on Forage |

---

## 🗂️ Repo structure

```
📦 financial-chatbot
├── 📁 task1-data-analysis
│   ├── financial_analysis.ipynb   # the full analysis notebook
│   ├── financial_analysis.html    # exported version
│   ├── financial_data.csv         # extracted 10-K data
│   └── financial_data.xlsx
├── 📁 task2-chatbot
│   ├── chatbot.py                 # the chatbot 🤖
│   ├── test_chatbot.py            # test runner
│   ├── test_results.txt           # test output
│   ├── financial_data.csv
│   └── README.md                  # chatbot docs
├── 📁 certificate                 # Forage certificate of completion
└── README.md
```

---

## 🔬 Task 1: Data Extraction & Analysis

I pulled key figures from the 10-K filings, loaded them into **pandas**, and calculated:

- 📈 Year-over-year growth for every metric (`groupby('Company').pct_change()`)
- 💰 Net margin, equity, and liabilities-to-assets ratio
- 🔄 Cash conversion (operating cash flow ÷ net income)
- 📐 Revenue and net income CAGR

### 🔍 What the data showed

| Company | Revenue CAGR | Net Income CAGR | Net Margin FY25 | Vibe |
|---|---|---|---|---|
| 🟦 **Microsoft** | ~15.3% | ~18.6% | ~36% | Steady compounding machine |
| 🍎 **Apple** | ~4.2% | ~7.5% | ~27% | Biggest revenue, slower growth |
| 🚗 **Tesla** | ~-1.0% | ~-49.7% | ~4% | Flat revenue, shrinking margin |

> 💡 **Key insight:** Tesla's revenue barely moved, but its margin collapsed from ~15% to ~4%. Raw dollars hide the story that ratios reveal.

---

## 🤖 Task 2: The Chatbot

A rule-based chatbot that matches keywords, spots the **company** and **year** in your question, and builds the answer from the data.

### 💬 What you can ask

| # | Query | Example |
|---|---|---|
| 1 | Total revenue | `What is Apple's total revenue in 2024?` |
| 2 | Net income change | `How has Tesla's net income changed over the last year?` |
| 3 | Assets & liabilities | `What are Microsoft's total assets and liabilities in 2023?` |
| 4 | Operating cash flow | `What is the operating cash flow?` |
| 5 | Best net margin | `Which company has the highest net margin?` |

### 🎬 Demo

```text
You: How has Tesla's net income changed over the last year?
Bot: Tesla: net income decreased by $3.3B (46.5%) from $7.1B in FY2024 to $3.8B in FY2025.

You: Which company has the highest net margin?
Bot: In FY2024, Microsoft had the highest net margin (36.0%). Ranking: Microsoft 36.0%, Apple 24.0%, Tesla 7.3%.

You: Who will win the World Cup?
Bot: Sorry, I can only provide information on predefined queries. Type 'help' to see them.
```

### 🧠 How it works

```
User question ➜ lowercase ➜ detect company & year ➜ keyword intent match ➜ pandas lookup ➜ formatted answer
                                                          └─ no match ➜ helpful fallback message
```

---

## 🚀 Quick start

```bash
# 1. clone
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. install
pip install pandas matplotlib notebook

# 3. explore the analysis
jupyter notebook task1-data-analysis/financial_analysis.ipynb

# 4. talk to the bot
cd task2-chatbot
python chatbot.py
```

---

## ⚠️ Limitations (being honest)

- Keyword matching, **not** true NLP: no paraphrase understanding, no memory of past questions
- Only 3 companies, 3 fiscal years, 5 metrics
- Fiscal years end in different months (MSFT Jun · AAPL Sep · TSLA Dec), so cross-company comparisons are approximate
- Figures were entered manually and should be verified against the original 10-Ks; Tesla FY2025 balance-sheet and cash-flow fields are incomplete
- Not financial advice

## 🔮 What's next

- [ ] Swap keyword rules for an LLM / intent classifier
- [ ] Pull data straight from SEC EDGAR
- [ ] Cite the exact 10-K page for every number
- [ ] Add conversation memory (state management)
- [ ] Flask / Streamlit web UI

---

## 🏅 Certificate

Completed the **BCG X GenAI Job Simulation** on Forage (October 16, 2026). See the `certificate/` folder.

---

<div align="center">

### 👋 Let's connect

**Vaibhav Sable** · [LinkedIn](https://www.linkedin.com/in/your-profile) · [GitHub](https://github.com/your-username)

⭐ *If this helped you, drop a star!* ⭐

</div>

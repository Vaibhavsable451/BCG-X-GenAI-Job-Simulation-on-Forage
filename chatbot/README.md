# Financial Chatbot Prototype

A rule-based command-line chatbot that answers predefined questions about Microsoft, Tesla and Apple (FY2023–FY2025), using data extracted from their 10-K filings in Task 1.

## Files
- `chatbot.py` – chatbot logic (`simple_chatbot(query)` plus an interactive loop)
- `financial_data.csv` – data source (USD millions)
- `test_chatbot.py` – runs sample queries
- `test_results.txt` – output of the test run
- `README.md` – this documentation

## How to run
```
pip install pandas
python chatbot.py          # interactive; type 'help' or 'quit'
python test_chatbot.py     # regenerate test_results.txt
```

## How it works
1. The CSV is loaded with pandas.
2. The user's text is lower-cased and scanned for a **company name** (default: all three) and a **year** 2023–2025 (default: latest available).
3. If/else keyword matching picks one of five query types, and a function builds the answer from the data (figures shown in $ billions; changes calculated on the fly).
4. Anything unrecognised returns a polite fallback message.

## Supported queries
| # | Example | Keywords |
|---|---|---|
| 1 | What is the total revenue? | revenue, sales |
| 2 | How has net income changed over the last year? | net income/profit + change, grow, over |
| 3 | What are the total assets and liabilities? | asset, liabilit |
| 4 | What is the operating cash flow? | cash flow |
| 5 | Which company has the highest net margin? | margin |

Company and year can be added to any of them, e.g. "What is Apple's total revenue in 2024?".

## Limitations
- Rule-based keyword matching, not AI/NLP: it does not understand paraphrases, typos or follow-up questions and has no memory.
- Covers only 3 companies, 3 fiscal years and 5 metrics.
- Fiscal years end in different months (Microsoft Jun, Apple Sep, Tesla Dec), so cross-company comparisons are approximate.
- Data was entered manually and must be verified against the 10-Ks. Tesla FY2025 assets, liabilities and operating cash flow are missing, so the bot falls back to FY2024 for those (and says which year it used).
- "Highest net margin" defaults to FY2024, the latest year with complete data.
- Not financial advice.

## Future improvements
Use an LLM or intent classifier for natural language, retrieve data directly from SEC EDGAR, cite filing pages in answers, and add more metrics and companies.

"""Rule-based financial chatbot prototype (Microsoft, Tesla, Apple; FY2023-FY2025).

Answers 5 predefined query types using data extracted from 10-K filings.
Run:  python chatbot.py          (interactive command line)
"""
import re
import pandas as pd

DATA_FILE = "financial_data.csv"
df = pd.read_csv(DATA_FILE).sort_values(["Company", "Year"])
COMPANIES = list(df["Company"].unique())

HELP = (
    "I can answer these questions (add a company and/or year if you like):\n"
    "  1. What is the total revenue?\n"
    "  2. How has net income changed over the last year?\n"
    "  3. What are the total assets and liabilities?\n"
    "  4. What is the operating cash flow?\n"
    "  5. Which company has the highest net margin?\n"
    "Example: 'What is Apple's total revenue in 2024?'"
)


def money(millions):
    """Format USD millions as $X.XB."""
    return f"${millions / 1000:,.1f}B"


def find_companies(q):
    found = [c for c in COMPANIES if c.lower() in q]
    return found or COMPANIES          # no company named -> all three


def find_year(q):
    m = re.search(r"\b(2023|2024|2025)\b", q)
    return int(m.group(1)) if m else None


def get_row(company, metric, year=None):
    """Latest row (or the requested year) where the metric is available."""
    sub = df[(df["Company"] == company)].dropna(subset=[metric])
    if year is not None:
        sub = sub[sub["Year"] == year]
    return None if sub.empty else sub.iloc[-1]


def answer_metric(q, metric, label):
    year, lines = find_year(q), []
    for c in find_companies(q):
        r = get_row(c, metric, year)
        if r is None:
            lines.append(f"{c}: {label} is not available for {year or 'the requested period'}.")
        else:
            lines.append(f"{c}, {r['Fiscal Period']}: {label} was {money(r[metric])}.")
    return "\n".join(lines)


def answer_net_income_change(q):
    lines = []
    for c in find_companies(q):
        sub = df[df["Company"] == c].dropna(subset=["Net Income"])
        year = find_year(q)
        if year is not None:
            sub = sub[sub["Year"] <= year]
        if len(sub) < 2:
            lines.append(f"{c}: not enough data to compare years.")
            continue
        prev, cur = sub.iloc[-2], sub.iloc[-1]
        diff = cur["Net Income"] - prev["Net Income"]
        pct = diff / prev["Net Income"] * 100
        word = "increased" if diff > 0 else "decreased"
        lines.append(f"{c}: net income {word} by {money(abs(diff))} ({abs(pct):.1f}%) "
                     f"from {money(prev['Net Income'])} in FY{int(prev['Year'])} "
                     f"to {money(cur['Net Income'])} in FY{int(cur['Year'])}.")
    return "\n".join(lines)


def answer_assets_liabilities(q):
    year, lines = find_year(q), []
    for c in find_companies(q):
        ra, rl = get_row(c, "Total Assets", year), get_row(c, "Total Liabilities", year)
        if ra is None or rl is None:
            lines.append(f"{c}: assets/liabilities are not available for {year or 'the latest year'}.")
        else:
            lines.append(f"{c} (FY{int(ra['Year'])}): total assets {money(ra['Total Assets'])}, "
                         f"total liabilities {money(rl['Total Liabilities'])}.")
    return "\n".join(lines)


def answer_best_margin(q):
    year = find_year(q) or 2024    # 2024 is the latest year with complete data for all three
    sub = df[df["Year"] == year].dropna(subset=["Total Revenue", "Net Income"]).copy()
    sub["margin"] = sub["Net Income"] / sub["Total Revenue"] * 100
    best = sub.loc[sub["margin"].idxmax()]
    ranking = ", ".join(f"{r.Company} {r.margin:.1f}%" for r in sub.sort_values("margin", ascending=False).itertuples())
    return f"In FY{year}, {best['Company']} had the highest net margin ({best['margin']:.1f}%). Ranking: {ranking}."


def simple_chatbot(user_query):
    q = user_query.lower().strip().replace("'s", "")
    if not q:
        return "Please type a question. Type 'help' to see what I can answer."
    if q in ("help", "?", "hi", "hello"):
        return HELP
    if "margin" in q:
        return answer_best_margin(q)
    if "net income" in q or "profit" in q or "earnings" in q:
        if any(w in q for w in ("change", "grow", "growth", "increase", "decrease", "over")):
            return answer_net_income_change(q)
        return answer_metric(q, "Net Income", "net income")
    if "revenue" in q or "sales" in q:
        return answer_metric(q, "Total Revenue", "total revenue")
    if "asset" in q or "liabilit" in q:
        return answer_assets_liabilities(q)
    if "cash flow" in q or "operating cash" in q:
        return answer_metric(q, "Operating Cash Flow", "operating cash flow")
    return "Sorry, I can only provide information on predefined queries. Type 'help' to see them."


if __name__ == "__main__":
    print("Financial Chatbot (Microsoft, Tesla, Apple). Type 'help' for options, 'quit' to exit.")
    while True:
        try:
            text = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            break
        if text.strip().lower() in ("quit", "exit"):
            break
        print("Bot:", simple_chatbot(text))

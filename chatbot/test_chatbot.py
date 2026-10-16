"""Runs sample queries and writes the output to test_results.txt."""
from chatbot import simple_chatbot

TESTS = [
    "What is the total revenue?",
    "What is Apple's total revenue in 2024?",
    "How has net income changed over the last year?",
    "How has Tesla's net income changed over the last year?",
    "What are the total assets and liabilities?",
    "What are Microsoft's total assets and liabilities in 2023?",
    "What is the operating cash flow?",
    "Which company has the highest net margin?",
    "help",
    "Who will win the World Cup?",
    "",
]
with open("test_results.txt", "w") as f:
    for t in TESTS:
        out = f"Q: {t!r}\nA: {simple_chatbot(t)}\n" + "-" * 60 + "\n"
        print(out, end=""); f.write(out)

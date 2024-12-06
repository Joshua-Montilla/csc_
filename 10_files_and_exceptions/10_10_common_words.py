from pathlib import Path

path = Path("10_files_and_exceptions/book.txt")

text = path.read_text()
wordcount = text.lower().count(" a ")
print(f"'a' appears {wordcount} times")
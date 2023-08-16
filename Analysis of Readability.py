import os
import csv
import re
from collections import Counter
import nltk
from nltk.corpus import words as nltk_words

nltk.download("punkt")
nltk.download("words")
data_dir = "Data Extracted"
def count_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return len(sentences)
def calculate_avg_sentence_length(text):
    words = nltk.word_tokenize(text)
    sentences = count_sentences(text)
    return len(words) / sentences if sentences > 0 else 0

def calculate_percentage_complex_words(text):
    complex_words = set(nltk_words.words())
    words = nltk.word_tokenize(text)
    complex_word_count = sum(1 for word in words if word.lower() in complex_words)
    return (complex_word_count / len(words)) * 100 if len(words) > 0 else 0

def calculate_fog_index(avg_sentence_length, percentage_complex_words):
    return 0.4 * (avg_sentence_length + percentage_complex_words)

input_csv_path = "Output Data Structure.csv"

rows = []

with open(input_csv_path, "r", newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX"]

    for row in reader:
        url_id = row["URL_ID"]
        filename = os.path.join(data_dir, f"{url_id}.txt")

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read()

                avg_sentence_length = calculate_avg_sentence_length(text)
                percentage_complex_words = calculate_percentage_complex_words(text)
                fog_index = calculate_fog_index(avg_sentence_length, percentage_complex_words)

                row["AVG SENTENCE LENGTH"] = avg_sentence_length
                row["PERCENTAGE OF COMPLEX WORDS"] = percentage_complex_words
                row["FOG INDEX"] = fog_index

        rows.append(row)

with open(input_csv_path, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("CSV file updated successfully.")

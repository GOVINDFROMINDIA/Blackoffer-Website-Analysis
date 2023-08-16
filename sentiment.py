import os
import csv

positive_words_file = os.path.join('MasterDictionary', 'positive-words.txt')
negative_words_file = os.path.join('MasterDictionary', 'negative-words.txt')

positive_words = set()
negative_words = set()

with open(positive_words_file, 'r') as f:
    positive_words.update(f.read().splitlines())

with open(negative_words_file, 'r') as f:
    negative_words.update(f.read().splitlines())

csv_file_path = 'Output Data Structure.csv'
preprocessed_dir = 'Preprocessed'

data = []

with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]


for row in data:
    url_id = row['URL_ID']
    preprocessed_file_path = os.path.join(preprocessed_dir, f"{url_id}.txt")

    try:
        with open(preprocessed_file_path, 'r', encoding='utf-8') as preprocessed_file:
            text = preprocessed_file.read()
            positive_score = sum(1 for word in text.split() if word in positive_words)
            negative_score = -sum(1 for word in text.split() if word in negative_words)

            row['POSITIVE SCORE'] = positive_score
            row['NEGATIVE SCORE'] = negative_score
    except Exception as e:
        print(f"Error processing {preprocessed_file_path}: {e}")

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Scores updated in CSV file.")

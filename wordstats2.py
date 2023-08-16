import pandas as pd
import nltk
from nltk.corpus import stopwords
import os
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

csv_file = 'Output Data Structure.csv'
data = pd.read_csv(csv_file)

stop_words = set(stopwords.words('english'))

for index, row in data.iterrows():
    url_id = row['URL_ID']
    text_file_path = f'Data Extracted/{url_id}.txt'
    if os.path.exists(text_file_path):
        print("Text File Path:", text_file_path)
        with open(text_file_path, 'r', encoding='utf-8') as text_file:
            text = text_file.read()
        words = word_tokenize(text)
        cleaned_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
        complex_word_count = sum(len(word) > 2 for word in cleaned_words)
        total_word_count = len(cleaned_words)
        
        data.loc[index, 'COMPLEX WORD COUNT'] = complex_word_count
        data.loc[index, 'WORD COUNT'] = total_word_count
    else:
        print(f"Text file not found for URL_ID: {url_id}. Skipping.")

data.to_csv(csv_file, index=False)

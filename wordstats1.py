import os
import pandas as pd
from textstat import syllable_count
from collections import Counter
data_dir = "Data Extracted"
output_csv = "Output Data Structure.csv"
metrics_dict = {
    'URL_ID': [],
    'AVG NUMBER OF WORDS PER SENTENCE': [],
    'SYLLABLE PER WORD': [],
    'PERSONAL PRONOUNS': [],
    'AVG WORD LENGTH': []
}

for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        url_id = filename.replace('.txt', '')
        with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as file:
            content = file.read()
            sentences = content.split('.') 
            words = content.split() 

        
            num_sentences = len(sentences)
            num_words = len(words)
            total_syllables = sum(syllable_count(word) for word in words)
            personal_pronoun_count = Counter(words)['I'] + Counter(words)['we'] + Counter(words)['my'] + \
                                     Counter(words)['ours'] + Counter(words)['us']
            total_characters = sum(len(word) for word in words)

            
            metrics_dict['URL_ID'].append(url_id)
            metrics_dict['AVG NUMBER OF WORDS PER SENTENCE'].append(num_words / num_sentences)
            metrics_dict['SYLLABLE PER WORD'].append(total_syllables / num_words)
            metrics_dict['PERSONAL PRONOUNS'].append(personal_pronoun_count)
            metrics_dict['AVG WORD LENGTH'].append(total_characters / num_words)


data = pd.read_csv(output_csv)
for idx, row in data.iterrows():
    url_id = str(row['URL_ID'])  
    if url_id in metrics_dict['URL_ID']:
        matching_idx = metrics_dict['URL_ID'].index(url_id)
        data.at[idx, 'AVG NUMBER OF WORDS PER SENTENCE'] = metrics_dict['AVG NUMBER OF WORDS PER SENTENCE'][matching_idx]
        data.at[idx, 'SYLLABLE PER WORD'] = metrics_dict['SYLLABLE PER WORD'][matching_idx]
        data.at[idx, 'PERSONAL PRONOUNS'] = metrics_dict['PERSONAL PRONOUNS'][matching_idx]
        data.at[idx, 'AVG WORD LENGTH'] = metrics_dict['AVG WORD LENGTH'][matching_idx]

data.to_csv(output_csv, index=False)

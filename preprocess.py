import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tqdm import tqdm  

nltk.download('punkt')
nltk.download('stopwords')

stop_words_files = [
    'StopWords_Auditor.txt',
    'StopWords_Currencies.txt',
    'StopWords_DatesandNumbers.txt',
    'StopWords_Generic.txt',
    'StopWords_GenericLong.txt',
    'StopWords_Geographic.txt',
    'StopWords_Names.txt'
]

stop_words = set()
for file in stop_words_files:
    file_path = os.path.join('StopWords', file)
    with open(file_path, 'r') as f:
        stop_words.update(f.read().splitlines())

data_extracted_dir = 'Data Extracted'
preprocessed_dir = 'Preprocessed'

if not os.path.exists(preprocessed_dir):
    os.makedirs(preprocessed_dir)

for root, dirs, files in os.walk(data_extracted_dir):
    for file_name in tqdm(files, desc="Processing files"):
        input_file_path = os.path.join(root, file_name)
        output_file_path = os.path.join(preprocessed_dir, file_name)

        try:
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                text = input_file.read()
                words = word_tokenize(text)
                filtered_words = [word for word in words if word.lower() not in stop_words]
                preprocessed_text = ' '.join(filtered_words)
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(preprocessed_text)
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("Text preprocessing complete.")

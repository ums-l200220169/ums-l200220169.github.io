import re
import pandas as pd

def clean_whatsapp_text(input_file, output_file):
    def preprocess_message(text):
        text = re.sub(r'^\d{2}/\d{2}/\d{4}, \d{2}:\d{2} - ', '', text)
        text = re.sub(r'^[^:]+: ', '', text)
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        text = re.sub(r'[^\w\s.,?!]', '', text)
        text = text.lower().strip()
        return text
    with open(input_file, 'r', encoding='utf-8') as f:
        messages = f.readlines()
    cleaned_messages = [
        msg for msg in map(preprocess_message, messages) 
        if len(msg.split()) > 3  
    ]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_messages))
    
    print(f"Berhasil membersihkan {len(cleaned_messages)} pesan")


clean_whatsapp_text('data_wa2.txt', 'data_wa2.csv')
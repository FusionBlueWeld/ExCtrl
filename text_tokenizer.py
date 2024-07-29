import csv
import torch
from transformers import AutoTokenizer, AutoModel
import torch.nn.functional as F

# Tokenizer and model setup
tokenizer = AutoTokenizer.from_pretrained('intfloat/multilingual-e5-large')
model = AutoModel.from_pretrained('intfloat/multilingual-e5-large')

def average_pool(last_hidden_states: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

# Load the CSV file
with open('output.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    rows = list(reader)

total_rows = len(rows)
processed_rows = []

for i, row in enumerate(rows):
    text = row[4]  # 5th column (0-based index)
    input_text = f'query: {text}'
    
    # Tokenize and get token counts
    batch_dict = tokenizer([input_text], max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**batch_dict)
    token_count = batch_dict['input_ids'].shape[1]
    
    # Append token count to row
    row.append(str(token_count))
    processed_rows.append(row)
    
    # Print progress
    print(f"Processing {i + 1}/{total_rows}")

# Write the results back to a new CSV file
with open('output_with_token_counts.csv', mode='w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(processed_rows)

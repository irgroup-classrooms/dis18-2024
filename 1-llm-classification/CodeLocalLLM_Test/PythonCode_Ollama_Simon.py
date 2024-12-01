import csv
import requests
import json
import os

#Variabeln für das Skript, entsprechend ersetzen
csv_file_path = '/Users/alex/Taxonomy_LLM/queries_en_test_simoncomma.csv'
api_url = "http://localhost:11434/api/generate" 
model_name = "llama3.2"
max_length = 200
rows = []
row_counter = 1
base, ext = os.path.splitext(csv_file_path)
new_csv_file_path = f"{base}_updated{ext}"

with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

for row in rows:
    payload = {
        "model": model_name,
        "prompt": row['Prompt'] + '. Give a really short answer which contains only one word',
    }
    response = requests.post(api_url, json=payload)
    lines = response.text.strip().split("\n")
    answers = [json.loads(line).get("response", "") for line in lines if line.strip()]
    full_answer = " ".join(answers).strip()
    row['Answer'] = full_answer[:max_length]
    print("Zeile: " + str(row_counter) + " geladen")
    row_counter += 1

#Schreibt Ergebnisse in eine neue csv
with open(new_csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated CSV file created at: {new_csv_file_path}")

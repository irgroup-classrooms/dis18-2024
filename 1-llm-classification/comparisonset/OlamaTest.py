import csv
import requests
import json
import os

#Variabeln für das Skript, entsprechend ersetzen
csv_file_path = '/Users/alex/Taxonomy_LLM/Query_Ollama_Test.csv'
api_url = "http://localhost:11434/api/generate" 
model_name = "llama3.2"
max_length = 200
rows = []
row_counter = 1
base, ext = os.path.splitext(csv_file_path)
new_csv_file_path = f"{base}_updated{ext}"
context=".Try to be sure about it. Categorize the request into one of the following categories, responding only with the category name: time-independent (timeless information not tied to a specific time or event, e.g., definitions, recipes, general rules), explicit-time (requests with explicit time references, e.g., years, dates, specific periods), event (requests about specific events, e.g., festivals, historical occurrences, event names), ambiguous (requests with terms or phrases that allow multiple interpretations depending on context, e.g., Turkey could mean a country or bird), or timeliness (time-sensitive or current information, e.g., weather, stock prices, live updates). Categorization Process: 1. Look for explicit time references (e.g., years, dates). Assign to explicit-time if present. 2. Check for event-related terms. Assign to event if applicable. 3. If the request is timeless and not tied to time or events, assign to time-independent. 4. If the request is ambiguous, assign to ambiguous. 5. If the request requires real-time or current information, assign to timeliness. Only respond with the category name. Examples: What is the definition of gravity? → time-independent, Weather in Berlin tomorrow? → timeliness, Oktoberfest 2024 → explicit-time, Turkey → ambiguous."

with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

for row in rows:
    payload = {
        "model": model_name,
        "prompt": row['Prompt'] + context,
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

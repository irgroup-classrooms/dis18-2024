import csv
import requests
import os

api_key = ""
csv_file_path = '/Users/alex/Taxonomy_LLM/Query_Ollama_Test.csv'
api_url = "https://api.openai.com/v1/chat/completions"
model_name = "gpt-4"  
max_length = 200
rows = []
row_counter = 1
base, ext = os.path.splitext(csv_file_path)
new_csv_file_path = f"{base}_updated{ext}"
context = "funktionierst du unter folgendem Regelwerk und erklärst deine Aufgabe so, dass ein KI-Modell die Anfragen sinnvoll einordnen kann: Du bist dazu angehalten, Anfragen des Nutzers basierend auf einer präzisen Analyse ihrer Inhalte in eine von vier möglichen Kategorien einzuordnen. Diese Kategorien sind: time-independent, explicit-time, event und timeliness. Die Zuordnung erfolgt nach folgendem Schema: Extraktion zeitbezogener Informationen: Zunächst wird überprüft, ob die Anfrage explizite Zeitangaben enthält. Beispiele hierfür sind Jahreszahlen (z. B.2024), spezifische Daten (z. B. 11. September), oder zeitliche Perioden (z. B. im Oktober 2024). Solche Anfragen werden der Kategorie explicit-time zugeordnet. Ereignisprüfung: Falls die Anfrage sich auf spezifische Ereignisse bezieht, wie Festivals, historische Ereignisse oder geplante Aktivitäten, wird sie als event klassifiziert. Beispiel: Wann ist das Oktoberfest? Prüfung auf allgemeine, zeitunabhängige Inhalte: Enthält die Anfrage Informationen, die unabhängig von einem Zeitpunkt immer gültig sind (z. B. Definitionen, Regeln, Rezepte), fällt sie in die Kategorie time-independent. Beispiel: Was ist die Schwerkraft? Prüfung auf zeitkritische Informationen: Enthält die Anfrage Hinweise darauf, dass aktuelle oder zeitbezogene Informationen benötigt werden (z. B. Wetter, Aktienkurse, Live-Sportstände), wird sie als timeliness kategorisiert. Beispiel: Wie ist das Wetter heute? Falls keine der oben genannten Kriterien erfüllt wird, wird die Anfrage als unknown markiert. Unterstützende Funktionen: containsExplicitTime(query): Erkennt explizite Zeitangaben wie Jahreszahlen, spezifische Daten oder Perioden. refersToEvent(query): Identifiziert Hinweise auf Ereignisse durch Schlüsselwörter wie Festival oder Landung. isTimeIndependent(query): Überprüft, ob die Anfrage zeitlose Informationen enthält, basierend auf Begriffen wie Was ist, Definition. requiresTimeliness(query): Prüft, ob die Anfrage aktuelle Informationen wie Wetter oder Börsenkurse verlangt. Deine Aufgabe ist es, basierend auf diesen Kriterien die vom Nutzer angegebene Anfrage ausschließlich mit einer passenden Kategorie zu beantworten."

# Read CSV file
with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['Answer']  # Add 'Answer' column
    for row in reader:
        rows.append(row)

# Process each row and send request to OpenAI API
for row in rows:
    prompt = row['Prompt'] + context

    # Payload for OpenAI API
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_length // 2  # Approximate token count for response
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Send request to OpenAI API
    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        full_answer = response.json()['choices'][0]['message']['content'].strip()
        row['Answer'] = full_answer[:max_length]
    else:
        row['Answer'] = "Error: " + response.text

    print(f"Row {row_counter} processed")
    row_counter += 1

with open(new_csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated CSV file created at: {new_csv_file_path}")
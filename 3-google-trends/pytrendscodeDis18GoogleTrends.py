from pytrends.request import TrendReq
import pandas as pd

# Initialisierung der Pytrends-Anfrage
pytrends = TrendReq(hl='de')

# Variablen festlegen
keywords = []
cat = '0'
geo = 'DE'
gprop = ''

timeframes = ['today 5-y', 'today 12-m', 'today 3-m', 'today 1-m']

# Leeres DataFrame erstellen, in dem die Daten gesammelt werden
collected_data = pd.DataFrame()

# Excel-Datei mit den Abfragen einlesen
query = pd.read_excel(r"C:\Users\User\Documents\TH-Köln\fünftes Semester\DIS 18\google_trends_query.xlsx")

def check_trends():
    """
    Diese Funktion erstellt eine Payload für die Google Trends API und holt die Interesse-über-Zeit-Daten. Die Daten werden
    an das DataFrame "collected_data" angehängt.
    """
    global collected_data  # Zugriff auf das globale DataFrame
    
    # Payload für die Keywords erstellen
    pytrends.build_payload(keywords, cat, timeframes[1], geo, gprop)
    
    # Interesse-über-Zeit-Daten abrufen
    data = pytrends.interest_over_time()
    
    # Wenn "date" in den Spalten ist, die "date"-Spalte zurücksetzen
    if 'date' in data.columns:
        data.reset_index(inplace=True)
    
    # Überprüfen, ob "isPartial" vorhanden ist, und die Spalte entfernen
    if 'isPartial' in data.columns:
        data = data.drop(columns=['isPartial'])
    
    # Daten an das globale DataFrame als Spalten anhängen
    if collected_data.empty:
        collected_data = data
    else:
        collected_data = pd.concat([collected_data, data], axis=1)

# Schleife, die alle Keywords aus der Excel-Datei abruft und Trends-Daten sammelt
for i in query.columns:
    all_keywords = query[i].dropna().tolist()  # Liste der Werte in der Spalte (ohne NaN)
    for kw in all_keywords:
        keywords.append(kw)  # Keyword zur Liste hinzufügen
        check_trends()  # Trends-Daten sammeln
        keywords.pop()  # Keyword aus der Liste entfernen

# Gesammelte Daten in eine Excel-Datei exportieren
collected_data.to_excel(r"C:\Users\User\Documents\TH-Köln\fünftes Semester\DIS 18\Daten_neu.xlsx", index=False)

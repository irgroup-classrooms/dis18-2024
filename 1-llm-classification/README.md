# Klassifizieren von temporalen Querys mit LLMs

- Gemeinsam erstellte Taxonomie als Grundlage für einen Prompt
- Prompt tuning: Single vs. multi-shot
- Implementierung zur Automatisierung der Klassifikation
- Vergleich zu unseren eigenen Ergebnissen


## Queries
Die Datei `queries.csv` enthält einige Queries aus dem LongEval Datensatz. Diese haben aber keine Topics und sind recht kurz.
Interessant könnten auch die Topics aus Robust 04 sein. Diese könnt ihr euch einfach über ir_datasets laden:


```bash
pip install ir_datasets
```

```python
import ir_datasets

dataset = ir_datasets.load("disks45/nocr/trec-robust-2004")
for query in dataset.queries_iter():
    break
```


# Query Types:

## Not Temporal
A query is classified as Not Temporal if it does not contain any direct or indirect references to time.
The query has no direct time reference. This means the query does not explicitly mention specific time spans (e.g., dates, years, or time periods) or implicitly include temporal cues (e.g., words like "latest," "recent," "now," "oldest," etc.). The relevance of results remains static and is independent of the time at which the query is issued.

Examples: Informatik, secure password, definition IR, What is a computer algorithm?, Chess rules, Recipe strawberry cake, definition of freedom


## Explicit Temporal
A query is classified as Explicitly Temporal when it explicitly specifies a temporal context through a clear reference to a year, date, or defined timeframe. The temporal context needs to be clearly articulated and non-ambiguous. The relevance of the results is strictly tied to this specified temporal context, and only content that directly pertains to the stated timeframe is considered accurate and relevant. 

Examples:  Time shift in October 2024, 11th of September, European championship 2024, last US presidential election


## Implicit Temporal
A query is classified as Implicitly Temporal when it directly connects to points in time without explicitly mentioning specific dates, years, or timeframes. The temporal context is inferred based on the nature of the query. In such cases, the relevance of results typically focuses on the most recent, upcoming, or contextually significant occurrences.

Example: European Championship, tsunami, Oktoberfest Munich, Moon landing Apollo 13, Volcanic eruption in Iceland, Presidential Inauguration, weather, stock market, sports league results, open restaurants 


## Temporal Ambiguous
A query is classified as Ambiguous Temporal when its meaning and relevance vary significantly based on the point in time it is issued. The ambiguity is thereby dependent on the point in time. 

The temporal context (e.g., season, current events, or cultural cycles) heavily influences the interpretation of the query and determines the most relevant results. This class captures queries where the same term or phrase can refer to different concepts or contexts at different times. For example, the query turkey most likely means the Thanksgiving dish in winter but the holiday destination in summertime. 

Example: Turkey, Star Wars, Wiesen, Apple, Easter Eggs

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
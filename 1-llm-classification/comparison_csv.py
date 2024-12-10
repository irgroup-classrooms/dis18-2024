import csv
import matplotlib.pyplot as plt
import seaborn as sns

rows1 = []
rows2 = []
same = []
notsame = []


file1_path = "/Users/alex/Taxonomy_LLM/Query_Ollama_Test_updated.csv"
file2_path = "/Users/alex/Taxonomy_LLM/Taxonomie_Einteilung.csv"

with open(file1_path, mode='r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    for row in reader:
        rows1.append(row)    

with open(file2_path, mode='r') as file2:
    reader = csv.DictReader(file2)
    fieldnames = reader.fieldnames
    for row in reader:
        rows2.append(row)    

if len(rows1) == len(rows2):
    n = len(rows1)
x = 0

while x < n:
    answer = str(rows1[x]) + " ; " + str(rows2[x])
    print(str(rows1[x]).replace(" ", ""))
    print(str(rows2[x]).replace(" ", ""))
    if str(rows1[x]).replace(" ", "") == str(rows2[x]).replace(" ", ""):
        same.append(rows1[x])
    else:
        notsame.append(answer)
    x += 1

print("Überschneidungen: ")
print(same)
print("Unterscheidungen: ")
print(notsame)
print()
print()
print()
print()
print(len(same))
print(len(notsame))
print(len(same)/50*100)
print(len(notsame)/50*100)
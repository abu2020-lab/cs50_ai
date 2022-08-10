#!/usr/bin/env python3

import csv


filename = "family0.csv"
data = dict()
with open(filename) as f:
    reader = csv.DictReader(f)
    #print(reader)
    for row in reader:
    	name = row["name"]
    	data[name] = {
            "name": name,
            "mother": row["mother"] or None,
            "father": row["father"] or None,
            "trait": (True if row["trait"] == "1" else
                      False if row["trait"] == "0" else None)
            }
print(data)

        

#!/usr/bin/env python3


import csv
import sys

#from util import Node, StackFrontier, QueueFrontier

people = {}


def load_data():
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
        	people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
    print(people)


load_data()
# This file handles loading data from CSV files

import pandas as pd
from smart_courier.models import Package, Van

def load_packages_csv(path):
    # Load package data from CSV file
    df = pd.read_csv(path)
    return [
        Package(
            row['id'],
            row['weight'],
            row['value'],
            row['priority'],
            row['destination']
        )
        for _, row in df.iterrows()
    ]

def load_vans_csv(path):
    # Load van data from CSV file
    df = pd.read_csv(path)
    return [Van(row['id'], row['capacity']) for _, row in df.iterrows()]

def load_edge_list_csv(path):
    # Load graph edges from CSV file
    df = pd.read_csv(path)
    return [(row['source'], row['target'], row['weight']) for _, row in df.iterrows()]

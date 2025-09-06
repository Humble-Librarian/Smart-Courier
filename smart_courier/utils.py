import pandas as pd
from smart_courier.models import Package, Van

def load_packages_csv(path):
    df = pd.read_csv(path)
    return [
        Package(
            row['id'],
            row['weight'],
            row['value'],
            row['priority'],
            row['destination']   # NEW
        )
        for _, row in df.iterrows()
    ]

def load_vans_csv(path):
    df = pd.read_csv(path)
    return [Van(row['id'], row['capacity']) for _, row in df.iterrows()]

def load_edge_list_csv(path):
    df = pd.read_csv(path)
    return [(row['source'], row['target'], row['weight']) for _, row in df.iterrows()]

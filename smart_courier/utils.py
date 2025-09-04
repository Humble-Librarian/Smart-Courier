import csv
from typing import List
from .models import Package, Van

def load_packages_csv(path: str) -> List[Package]:
    res=[]; 
    with open(path) as f:
        r=csv.DictReader(f)
        for row in r:
            res.append(Package(pid=row['id'],weight=int(row['weight']),value=float(row['value']),destination=row['destination'],priority=int(row.get('priority',0))))
    return res

def load_vans_csv(path: str) -> List[Van]:
    res=[]
    with open(path) as f:
        r=csv.DictReader(f)
        for row in r:
            res.append(Van(vid=row['id'],capacity=int(row['capacity']),start=row.get('start','DEPOT')))
    return res

def load_edge_list_csv(path: str):
    edges=[]
    with open(path) as f:
        r=csv.DictReader(f)
        for row in r:
            edges.append((row['source'],row['destination'],float(row['distance'])))
    return edges

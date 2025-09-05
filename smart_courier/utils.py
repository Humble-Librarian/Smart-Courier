
import csv
from .models import Package, Van

def load_packages_csv(path):
    with open(path, newline='') as f:
        return [Package(int(r['id']), int(r['weight']), int(r['value']), int(r['priority'])) for r in csv.DictReader(f)]

def load_vans_csv(path):
    with open(path, newline='') as f:
        return [Van(int(r['id']), int(r['capacity'])) for r in csv.DictReader(f)]

def load_edge_list_csv(path):
    with open(path, newline='') as f:
        return [(r['u'], r['v'], int(r['w'])) for r in csv.DictReader(f)]

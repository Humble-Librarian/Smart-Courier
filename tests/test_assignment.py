# Test file for package assignment algorithms

from smart_courier.assignment import assign_packages_greedy
from smart_courier.models import Package, Van

def test_greedy():
    # Test greedy package assignment
    pkgs=[Package("p1",5,10,1,"B"),Package("p2",4,40,1,"C"),Package("p3",6,30,1,"D")]
    vans=[Van("Van1",10)]
    res = assign_packages_greedy(vans, pkgs)
    assert "Van1" in res

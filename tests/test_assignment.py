from smart_courier.assignment import assign_packages_greedy
from smart_courier.models import Package, Van
def test_greedy_assignment():
    pkgs=[Package(1,5,10),Package(2,4,40),Package(3,6,30)]
    vans=[Van(1,10)]
    result=assign_packages_greedy(vans,pkgs)
    assert 1 in result

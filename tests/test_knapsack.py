from smart_courier.knapsack import knapsack_01
from smart_courier.models import Package
def test_knapsack_simple():
    pkgs=[Package(1,5,10),Package(2,4,40),Package(3,6,30)]
    val,chosen=knapsack_01(pkgs,10)
    assert val>=40

from smart_courier.knapsack import knapsack_01
from smart_courier.models import Package
def test_knapsack_basic():
    pkgs = [Package("p1",3,60,1,"B"),Package("p2",2,100,1,"C"),Package("p3",4,120,1,"D")]
    val, chosen = knapsack_01(pkgs, 5)
    assert int(val) == 160

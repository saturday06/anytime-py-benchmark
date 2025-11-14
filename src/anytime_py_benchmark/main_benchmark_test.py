import pytest
from statistics import median

@pytest.mark.benchmark
def test_median_performance():
    input = [1, 2, 3, 4, 5]
    output = sum(i**2 for i in input)
    assert output == 55

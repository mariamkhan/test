import pytest
from index import Calculations


@pytest.mark.parametrize("input_FV, input_r, input_n, expected_PV",
                         [(1000, 10, 5, 620.92),
                          (100, 5, 1, 95.24),
                          (-50, 5, 2, -45.35),
                          (35, 5, 3, 30.23),
                          (-35, 5, 1, -33.33),
                          (50, 5, 1, 47.62)])
def test_PV_calculator(input_FV, input_r, input_n, expected_PV):
    # This unit test checks the PV values are as expected
    calculator = Calculations(input_FV, input_r, input_n)
    assert calculator.compute_present_value() == expected_PV

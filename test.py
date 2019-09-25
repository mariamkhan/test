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
    # Check the PV values are computed as expected
    calculator = Calculations(input_FV, input_r, input_n)
    assert calculator.compute_present_value() == expected_PV


@pytest.mark.parametrize("input_present_value_1, input_present_value_2,"
                         "input_rate_1,input_rate_2, expected_delta",
                         [(95.24, -45.35, 5, 5, None),
                          (467.29, 571.24, 7.0, 9.5, 41.58),
                          (571.24, -523.5, 9.5, 2.5, 156.39)])
def test_compute_delta(input_present_value_1, input_present_value_2,
                       input_rate_1, input_rate_2, expected_delta):
    # Check the Delta values are computed as expected
    assert Calculations.compute_delta(input_present_value_1,
                                      input_present_value_2, input_rate_1,
                                      input_rate_2) == expected_delta

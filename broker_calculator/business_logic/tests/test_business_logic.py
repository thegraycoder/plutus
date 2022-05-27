import unittest

from broker_calculator.business_logic.business_logic import get_brokerage


class TestGetBrokerage(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_brokerage(self):
        investment_type = "SIP"

        brokerage = get_brokerage()

    def tearDown(self) -> None:
        pass

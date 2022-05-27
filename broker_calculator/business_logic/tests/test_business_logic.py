import unittest
from unittest.mock import patch

from broker_calculator.business_logic import business_logic


class MockBroker:
    def __init__(self):
        self.brokerage = 0.0

    def get_brokerage_for_sip(self, broker_name, interval, start_date, end_date, amount, currency):
        return self.brokerage


class TestGetBrokerageForSIP(unittest.TestCase):
    def setUp(self) -> None:
        self.broker_name = 'Broker'
        self.interval = 'monthly'
        self.start_date = '2022-01-01'
        self.end_date = '2022-02-01'
        self.amount = '1000'
        self.currency = 'USD'

    @patch('broker_calculator.models.broker.Broker', new=MockBroker)
    def test_get_brokerage_for_sip(self):
        brokerage = business_logic.get_brokerage_for_sip(
            broker_name=self.broker_name,
            interval=self.interval,
            start_date=self.start_date,
            end_date=self.end_date,
            amount=self.amount,
            currency=self.currency
        )
        self.assertEqual(brokerage, 0.0)

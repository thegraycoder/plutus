import datetime
import unittest
from unittest.mock import patch

import pytest

from broker_calculator.business_logic import business_logic


class MockBroker:
    def __init__(self):
        self.brokerage = 0.0

    def get_brokerage_for_sip(self, ticker, broker_name, interval, start_date, end_date, amount, currency):
        return self.brokerage


class MockBrokerWithoutSipImplementation:
    pass


class TestGetBrokerageForSIP(unittest.TestCase):
    def setUp(self) -> None:
        self.ticker = 'AAPL'
        self.broker_name = 'Broker'
        self.interval = 'monthly'
        self.start_date = datetime.date(2022, 1, 1)
        self.end_date = datetime.date(2023, 1, 1)
        self.amount = 1000.0
        self.currency = 'USD'

    @patch('broker_calculator.models.broker.Broker', new=MockBroker)
    def test_get_brokerage_for_sip(self):
        brokerage = business_logic.get_brokerage_for_sip(
            ticker=self.ticker,
            broker_name=self.broker_name,
            interval=self.interval,
            start_date=self.start_date,
            end_date=self.end_date,
            amount=self.amount,
            currency=self.currency
        )
        self.assertEqual(0.0, brokerage)

    def test_package_for_broker_does_exist(self):
        with pytest.raises(NotImplementedError) as nie:
            _ = business_logic.get_brokerage_for_sip(
                ticker=self.ticker,
                broker_name='RandomBroker',
                interval=self.interval,
                start_date=self.start_date,
                end_date=self.end_date,
                amount=self.amount,
                currency=self.currency
            )
        self.assertEqual('package broker_calculator.models.randombroker not found', str(nie.value))

    def test_broker_not_found_in_package(self):
        with pytest.raises(NotImplementedError) as nie:
            _ = business_logic.get_brokerage_for_sip(
                ticker=self.ticker,
                broker_name='BROKER',
                interval=self.interval,
                start_date=self.start_date,
                end_date=self.end_date,
                amount=self.amount,
                currency=self.currency
            )
        self.assertEqual('broker BROKER not found in the package broker_calculator.models.broker', str(nie.value))

    @patch('broker_calculator.models.broker.Broker', new=MockBrokerWithoutSipImplementation)
    def test_broker_does_not_implement_get_brokerage_for_sip(self):
        with pytest.raises(NotImplementedError) as nie:
            _ = business_logic.get_brokerage_for_sip(
                ticker=self.ticker,
                broker_name=self.broker_name,
                interval=self.interval,
                start_date=self.start_date,
                end_date=self.end_date,
                amount=self.amount,
                currency=self.currency
            )
        self.assertEqual('method get_brokerage_for_sip not implemented in broker Broker', str(nie.value))

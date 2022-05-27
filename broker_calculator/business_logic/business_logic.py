import logging
import importlib


def get_brokerage_for_sip(broker_name, interval, start_date, end_date, amount, currency):
    _module = f'broker_calculator.models.{broker_name.lower()}'
    try:
        module = importlib.import_module(_module)
        try:
            broker = getattr(module, broker_name)()
            try:
                return broker.get_brokerage_for_sip(broker_name, interval, start_date, end_date, amount, currency)
            except AttributeError as method_not_found:
                logging.debug(method_not_found)
                logging.error(f'broker {broker_name} should implement get_brokerage_for_sip function.')
                raise NotImplementedError(f'method get_brokerage_for_sip not implemented in broker {broker_name}')
        except AttributeError as err:
            logging.debug(err)
            logging.error(f'Attr err: broker with name {broker_name} should be in package called {broker_name.lower()}.')
            raise NotImplementedError(f'broker {broker_name} not found in the package {_module}')
    except ImportError:
        logging.error(f'Import err: you are trying to find class {broker_name} in package {_module} which does not '
                      f'exist.')
        raise NotImplementedError(f'package {_module} not found')


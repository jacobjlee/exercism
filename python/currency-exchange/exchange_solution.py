def exchange_money(budge: float, exchange_rate: float) -> float:
    """Exchange money to a foreign currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budge / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate the amount left of your starting currency after exchanging.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate the total value of the bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Calculate the number of bills that can be obtained from the amount.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return int(amount / denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """Calculate the amount that is "leftover", given the current denomination.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """Calculate the maximum value you can get.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # Calculate the effective exchange rate including spread
    effective_exchange_rate = exchange_rate * (1 + spread / 100)
    
    # Calculate the amount of money after exchanging
    exchanged_value = exchange_money(budget, effective_exchange_rate)
    
    # Calculate the number of bills you can obtain
    number_of_bills = get_number_of_bills(exchanged_value, denomination)
    
    # Calculate the maximum value you can get in terms of denomination
    max_value = get_value_of_bills(denomination, number_of_bills)
    
    return int(max_value)

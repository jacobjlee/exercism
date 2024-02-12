# Time the lasagna needs to be in the oven
EXPECTED_BAKE_TIME: int = 40  # minutes
PREPARATION_TIME: int = 2  # minutes


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the total preparation time in minutes.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - total preparation time (in minutes) required for the specified number of layers.

    This function calculates the total preparation time required based on the number
    of layers in the lasagna and the time required to prepare each layer.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    total_preparation_time: int = preparation_time_in_minutes(number_of_layers)
    
    return total_preparation_time + elapsed_bake_time

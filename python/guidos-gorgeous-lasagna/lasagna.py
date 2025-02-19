EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers in lasagna
    :return: int - overall time to prepare all layers

    Function that takes the number of layers of lasagna and 
    calculates its preparation time (no baking yet)
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param number_of_layers: int - number of layers in lasagna
    :param elapsed_bake_time: int - number of minutes lasagna already baking
    :return: int - overall time to bake all layers

    Function that takes the number of layers of lasagna and 
    calculates its baking time
    """
    return number_of_layers * 2 + elapsed_bake_time

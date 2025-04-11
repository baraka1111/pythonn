EXPECTED_BAKE_TIME = 40
 
    
def bake_time_remaining(minutes_baked):
    """Return the remaining minutes to bake."""
    return EXPECTED_BAKE_TIME - minutes_baked
def preparation_time_in_minutes(layers):
    """Return the preparation time in minutes based on the number of layers."""
    return layers * 2
def elapsed_time_in_minutes(layers, minutes_baked):
    """Return the total time elapsed in minutes, including preparation and baking time."""
    return preparation_time_in_minutes(layers) + minutes_baked

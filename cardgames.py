"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number, number + 1, number + 2]
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    pass


def concatenate_rounds(rounds_1, rounds_2):
    return  rounds_1 + rounds_2
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    pass


def list_contains_round(rounds, number):
    return number in rounds
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    pass


def card_average(hand):
    return sum(hand) / len(hand)
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    pass


def approx_average_is_average(hand):
    true_avg = card_average(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    
    return true_avg in (first_last_avg, middle_card)
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    pass


def average_even_is_average_odd(hand):
    even_cards = hand[::2]
    odd_cards = hand[1::2]
    
    if not odd_cards:  
        return False
        
    return sum(even_cards) / len(even_cards) == sum(odd_cards) / len(odd_cards)
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    pass


def maybe_double_last(hand):
    if hand and hand[-1] == 11:  
        hand[-1] *= 2
    return hand
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    pass

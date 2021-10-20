def get_rounds(number):
    """

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    if number in rounds:
        return True

    return False


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    order_of_middle_object = int(len(hand) / 2)
    middle = hand[order_of_middle_object]
    first = hand[0]
    last = hand[-1]

    approx_average = (first + last) / 2
    full_average_of_list = card_average(hand)

    if approx_average == full_average_of_list:
        return True

    if float(middle) == full_average_of_list:
        return True

    return False


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_list = hand[1::2]
    odd_list = hand[::2]
    average_of_even = card_average(even_list)
    average_of_odd = card_average(odd_list)
    if average_of_even == average_of_odd:
        return True

    return False


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last = hand[-1]
    if last == 11:
        except_last = hand[:-1]
        except_last.append(22)
        return except_last

    return hand

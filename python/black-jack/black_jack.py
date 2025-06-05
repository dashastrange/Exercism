"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
face_cards = ['J', 'K', 'Q']
blackjack_values = ['A', 'K', 'J', 'Q', '10']
cards_dict = {
        'A' : 1,
        'J' : 10,
        'K' : 10,
        'Q' : 10,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '10' : 10
    }

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in cards_dict:
        num_val_of_passed_card = cards_dict.get(card)

    return num_val_of_passed_card


def higher_card(card_one, card_two):
    """determine which card has a higher value in the hand.

    :param card_one:
    :param card_one, card_two: str - cards dealt in hand. See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'j', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'a' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card_one in cards_dict and card_two in cards_dict:
        c1 = cards_dict.get(card_one)
        c2 = cards_dict.get(card_two)

    if c1 < c2:
        return card_two
    if c1 > c2:
        return card_one
    if c1 == c2:
        return card_one, card_two
    else:
        return None


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one:
    :param card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    c1 = value_of_card(card_one)
    c2 = value_of_card(card_two)

    if card_one == 'A':
        c1 = 1
    if card_two == 'A':
        c2 = 1

    current_total = c1 + c2

    if card_one == 'A' or card_two == 'A':
        return 1

    if current_total + 11 > 21:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one: Str - card dealt. See below for values.
    :param card_two: str - card dealt. See below for values.
    :return: Bool - is the hand a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    bjh = ['10', 'J', 'K', 'Q']

    if (card_one == 'A' or card_two == 'A') and (card_one in bjh or card_two in bjh):
        return True
    else:
        return False



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one: Str - cards dealt.
    :param card_two: str - cards dealt.
    :return: Bool - can the hand be split into two pairs? (i.e., cards are of the same value).
    """

    if card_one == card_two:
        return True
    if card_one in face_cards and card_two in face_cards:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one:
    :param card_two: Str - first and second cards in hand.
    :return: bool - can the hand be doubled down? (i.e., totals 9, 10 or 11 points).
    """
    double_allowed = [9, 10, 11]
    num_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    str_num_cards = []
    hand = []

    if card_one == 'A' and card_two == 'A':
        return False

    for n in num_cards:
        str_num_cards.append(str(n))

    if card_one in blackjack_values:
        card_one = card_one
        hand.append(card_one)
    if card_one in str_num_cards:
        card_one = int(card_one)
        hand.append(card_one)

    if card_two in blackjack_values:
        card_two = card_two
        hand.append(card_two)
    if card_two in str_num_cards:
        card_two = int(card_two)
        hand.append(card_two)

    if ((hand[0] == 'A' and hand[1] in num_cards) or (hand[1] == 'A' and hand[0] in num_cards)
                                                  or (hand[1] == 'A' and hand[0] in face_cards)
                                                  or (hand[0] == 'A' and hand[1] in face_cards)):
        return True
    if (hand[0] in num_cards) and (hand[1] in num_cards) and (sum(hand) in double_allowed):
        return True
    if hand[0] in face_cards and hand[1] in face_cards:
        return True
    if (hand[0] in num_cards) and (hand[1] in num_cards) and (sum(hand) not in double_allowed):
        return False
    else:
        return False


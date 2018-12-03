# Chad Scott
# 12/3/18
# This program to play a gae of compare(war), which is a card game to see which card is higher in value
import deck


def make_a_deck():
    """
    This function makes a deck and shuffles it which allows the plaers to get 5 random cards
    :return:
    """
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    return deck_of_cards


def draw_a_card(deck_of_cards):
    """
    This function draws a random card from the shuffled deck of cards
    :param deck_of_cards:
    :return:
    """
    player_cards = []
    for x in range(5):
        player_cards.append(deck_of_cards.draw_a_card())
    return player_cards


def compare(card1, card2):
    """
    This function compares the two cards to see which card is higher in value
    :param card1:
    :param card2:
    :return:
    """
    return card1.compared_to(card2)


def main():
        player1score = 0
        player2score = 0
        deck_of_cards = make_a_deck()
        player1 = draw_a_card(deck_of_cards)
        player2 = draw_a_card(deck_of_cards)
        for x in range(5):
            print("Player 1 drew a", player1[x])
            print("Player 2 drew a", player2[x])
            winning_card = compare(player1[x], player2[x])
            print("The winning card is:", winning_card)
            print()
        if winning_card == player1[x]:
            print("Player 1 Wins")
            player1score += 1
        else:
            print("Player 2 Wins")
            player2score += 1
        if player1score > player2score:
            print("Player 1 has won the game")
        else:
            print("Player 2 has won the game")


main()
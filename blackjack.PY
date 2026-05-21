import random
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def create_deck():
    """Create a deck of cards."""
    return [f"{rank}{suit}" for suit in SUITS for rank in RANKS]


def shuffle_deck(deck):
    """Shuffle the deck."""
    random.shuffle(deck)


def draw_card(deck):
    """Draw a card from the deck."""
    return deck.pop()


def calculate_score(hand):
    """Calculate the score of a hand."""
    score = 0
    aces = 0

    for card in hand:
        rank = card[:-1]

        if rank in ["J", "Q", "K"]:
            score += 10
        elif rank == "A":
            score += 11
            aces += 1
        else:
            score += int(rank)

    # Convert aces from 11 to 1 if needed
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def show_hand(name, hand, hide_first=False):
    """Display a player's or dealer's hand."""

    if hide_first:
        print(f"{name}: [Hidden] {' '.join(hand[1:])}")

    else:
        score = calculate_score(hand)
        print(f"{name}: {' '.join(hand)}  --> {score} points")


def player_turn(deck, player_hand):
    """Handle the player's turn."""

    while True:
        score = calculate_score(player_hand)

        if score > 21:
            print("\nBust! You lose.")
            return False

        # Ask until valid answer
        while True:
            choice = input("\nHit or Stand? (h/s): ").lower()

            if choice in ["h", "s"]:
                break
            else:
                print("Invalid choice! Please type 'h' or 's'.")

        if choice == "h":
            new_card = draw_card(deck)
            player_hand.append(new_card)

            print(f"\nYou drew: {new_card}")
            show_hand("You", player_hand)

        elif choice == "s":
            return True


def dealer_turn(deck, dealer_hand):
    """Handle the dealer's turn."""

    print("\nDealer's turn...")
    show_hand("Dealer", dealer_hand)

    while calculate_score(dealer_hand) < 17:
        new_card = draw_card(deck)
        dealer_hand.append(new_card)

        print(f"Dealer drew: {new_card}")
        show_hand("Dealer", dealer_hand)


def determine_winner(player_hand, dealer_hand):
    """Determine the winner."""

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\n===== FINAL RESULT =====")
    print(f"You: {player_score}")
    print(f"Dealer: {dealer_score}")

    if dealer_score > 21:
        print("Dealer busts")

    elif player_score > dealer_score:
        print("You win")

    elif player_score < dealer_score:
        print("Dealer wins")

    else:
        print("Push")


def play_blackjack():
    """Run one full game of blackjack."""

    print("\n" + "=" * 40)
    print("BLACKJACK")
    print("=" * 40)

    deck = create_deck()
    shuffle_deck(deck)

    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    # Show starting hands
    show_hand("Dealer", dealer_hand, hide_first=True)
    show_hand("You", player_hand)

    # Instant blackjack
    if calculate_score(player_hand) == 21:
        print("\nBLACKJACK")
        show_hand("Dealer", dealer_hand)
        return

    # Player's turn
    if player_turn(deck, player_hand):

        # Dealer's turn
        dealer_turn(deck, dealer_hand)

        # Decide winner
        determine_winner(player_hand, dealer_hand)


def main():

    while True:
        play_blackjack()

        # Ask until valid answer
        while True:
            again = input("\nPlay again? (y/n): ").lower()

            if again in ["y", "n"]:
                break
            else:
                print("Invalid choice! Please type 'y' or 'n'.")

        if again == "n":
            print("Thanks for playing")
            break


if __name__ == "__main__":
    main()


def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:  # Keeps trying until player enters a valid suit
        suit = input("Pick a suit: ")
        if suit.lower() == 'd':
            active_suit = "Diamonds"
            got_suit = True
        elif suit.lower() == 's':
            active_suit = "Spades"
            got_suit = True
        elif suit.lower() == 'h':
            active_suit = "Hearts"
            got_suit = True
        elif suit.lower() == 'c':
            active_suit = "Clubs"
            got_suit = True
        else:
            print("Not a valid suit.  Try again.  ", end='')
    print("You picked",active_suit)

print("\nYour hand: ", end='')
for card in p_hand:
    print(card.short_name,end=' ')
print("   Up card: ", up_card.short_name)
if up_card.rank == '8':
    print("    Suit is", active_suit)

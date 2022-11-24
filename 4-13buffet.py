buffet = ('pounded yam', 'stuffed leg of lamb', 'love heart camembert', 'smoked salmon', 'Samosa')
for menu in buffet:
    print(menu)

#Invalid code; tupple is immutable
buffet[2] = 'Fried rice'
print(buffet)

buffet = ('pounded yam with egusi', 'samosa', 'stuffed leg of lamb', 'fried rice with greens', 'apapa in natura green foil')
for revised_menu in buffet:
    print(revised_menu)
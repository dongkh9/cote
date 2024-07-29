n = int(input())
card_list = list(map(int,input().split()))
m = int(input())
how_many_list = list(map(int,input().split()))

card_dict = {}
for card in card_list :
    if card not in card_dict :
        card_dict[card] = 1
    else :
        card_dict[card] += 1
for how_many in how_many_list :
    if how_many not in card_dict :
        print(0,end=' ')
    else :
        print(card_dict[how_many],end =' ')
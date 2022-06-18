def phazed_group_type(group):
    possible = []
    hand = []
    handnum = []
    numWild = 0
    check = 0
    col = False
    count5 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count = 0
    accumulation = 0
    wild = False
    hand = group
    length = len(hand)
    for s in hand:
        if s == 'AH' or s == 'AD' or s == 'AS' or s == 'AC':
            numWild = numWild + 1
            wild = True
    if wild:
        count = 1
        if numWild > 1:
            count5 = 2
            count2 = 2
        elif numWild == 1:
            count5 = 1
            count2 = 1
        if numWild > 5:
            count1 = 5
        else:
            count1 = numWild
    colorR = numWild
    colorB = numWild
    for card in hand:
        for comp in hand:
            if comp[0] != 'A' and card[0] != 'A' and card[0] == comp[0]:
                count = count + 1
                count5 = count5 + 1
                if count == 3 and length == 3:
                    possible.append(1)
                if count5 == 4 and length == 4:
                    possible.append(3)
            if card[0] != 'A' and comp[0] != 'A' and card[1] == comp[1]:
                count1 = count1 + 1
                if count1 == 7 and length == 7:
                    possible.append(2)
        if card[0] != 'A' and (card[1] == 'D' or card[1] == 'H'):
            count2 = count2 + 1
            colorR = colorR + 1
            if count2 == 4 and length == 4:
                possible.append(5)
            if colorR == length:
                col = True
        if card[0] != 'A' and (card[1] == 'S' or card[1] == 'C'):
            count3 = count3 + 1
            colorB = colorB + 1
            if colorB == length:
                col = True

        if card[0] == 'J':
            accumulation = accumulation + 11
            handnum.append(11)
        elif card[0] == 'Q':
            accumulation = accumulation + 12
            handnum.append(12)
        elif card[0] == 'K':
            accumulation = accumulation + 13
            handnum.append(13)
        elif card[0] == 'A':
            accumulation = accumulation + 1
            handnum.append(1)
        elif card[0] == '0':
            accumulation = accumulation + 10
            handnum.append(10)
        else:
            handnum.append(int(card[0]))
            accumulation = accumulation + int(card[0])
        if accumulation == 34:
            possible.append(6)
        if wild:
            count = 1
            if numWild > 1:
                count5 = 2
            elif numWild == 1:
                count5 = 1
            if numWild > 5:
                count1 = 5
            else:
                count1 = numWild
        else:
            count5 = 0
            count1 = 0
            count = 0
    if accumulation == 34 and col is True:
        possible.append(7)
    temp1 = 0
    if numWild > 6:
        numWild = 6
        temp1 = 6
        count4 = 6
    else:
        count4 = 0
        temp1 = numWild
    handnum.sort()
    if numWild != len(handnum):
        check = handnum[numWild]
        for x in handnum[numWild + 1:]:
            check = x - check
            if check == 1:
                count4 = count4 + 1
            else:
                if temp1 - check + 1 >= 0:
                    temp1 = temp1 - check + 1
                    count4 = count4 + check
            check = x

    if temp1 > 0:
        count4 = count4 + temp1
    if count4 == 7:
        possible.append(4)
    final_possible = []
    [final_possible.append(x) for x in possible if x not in final_possible]
    final_possible.sort()
    return final_possible


def phaze_phase_type(group):
    count1 = count3 = count4 = count6 = 0
    output = []
    possible = []
    for hand in group:
        out = phazed_group_type(hand)
        if 1 in out:
            count1 = count1 + 1
            if count1 == 2:
                possible.append(1)
        if 2 in out:
            possible.append(2)
        if 6 in out:
            count3 = count3 + 1
            if count3 == 2:
                possible.append(3)
        if 3 in out:
            count4 = count4 + 1
            output.append(3)
            if count4 == 2:
                possible.append(4)
        if 4 in out:
            possible.append(5)
        if 7 in out:
            count6 = count6 + 1
            if count6 == 2:
                possible.append(6)
        if 5 in out:
            output.append(5)
    if 5 in output:
        if 3 in output:
            possible.append(7)

    final = []
    [final.append(x) for x in possible if x not in final]
    final.sort()
    return final


print(phaze_phase_type([['4H', '5D', 'AC', '7H'], ['7H', '7C', 'AH', 'AS']]))



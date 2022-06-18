def forward_contact_trace(visit, ind, date_time, second_order=False):
    infect = []
    check = []
    infectdata = []
    time = ((date_time[1] * 60) + date_time[2])
    for j in visit:
        if j[0] == ind:
            if date_time[0] < j[2]:
                infect.append(j)
            elif date_time[0] == j[2]:
                if time < ((j[3] * 60) + j[4]):
                    infect.append(j)
        else:
            if j[0] != ind:
                check.append(j)

    newinfect = []
    for i in infect:
        for j in check:
            if i[1] == j[1] and i[2] == j[2]:
                start = ((i[3] * 60) + i[4]) - ((j[3] * 60) + j[4])
                end = ((i[5] * 60) + i[6]) - ((j[5] * 60) + j[6])
                if start >= 0:
                    start = ((i[3] * 60) + i[4])
                else:
                    start = ((j[3] * 60) + j[4])
                if end <= 0:
                    end = ((i[5] * 60) + i[6])
                else:
                    end = ((j[5] * 60) + j[6])
                if end - start > 0:
                    h = int(start / 60)
                    m = start - (60 * h)
                    newinfect.append(j[0])
                    infectdata.append((j[0], j[1], j[2], h, m))
    if second_order:
        for i in infectdata:
            temp = []
            temp = forward_contact_trace(check, i[0], (i[2], i[3], i[4]))
            newinfect = newinfect + temp

    finalist = []
    [finalist.append(x) for x in newinfect if x not in finalist]
    finalist.sort()
    return finalist


visits = [('Russel', 'Nutrity', 1, 5, 0, 6, 0),
          ('Russel', 'Foodigm', 2, 9, 0, 10, 0),
          ('Russel', 'Afforage', 2, 10, 0, 11, 30),
          ('Russel', 'Nutrity', 2, 11, 45, 12, 0),
          ('Russel', 'Liberry', 3, 13, 0, 14, 15),
          ('Natalya', 'Nutrity', 1, 5, 30, 6, 45),
          ('Natalya', 'Afforage', 2, 8, 15, 10, 0),
          ('Natalya', 'Nutrity', 4, 10, 10, 11, 45),
          ('Chihiro', 'Foodigm', 2, 9, 15, 9, 30),
          ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
          ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]

index = 'Russel'
d = (1, 9, 0)
output = []
output = forward_contact_trace(visits, index, d, True)
print(output)

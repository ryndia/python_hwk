def backward_contact_trace(visit, ind, date_time, window):
    infect = []
    check = []
    newinfect = []
    window = window - 1

    for v in visit:
        if ind == v[0] and date_time[0] == v[2]:
            infect.append(v)
        else:
            check.append(v)

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
                    newinfect.append(j[0])
                if window != 0:
                    out = []
                    out = backward_contact_trace(check, ind, (date_time[0] - 1, date_time[1], date_time[2]), window)
                    newinfect = newinfect + out
    return newinfect


visits = [('Russel', 'Foodigm', 2, 9, 0, 10, 0),
          ('Russel', 'Afforage', 2, 10, 0, 11, 30),
          ('Russel', 'Nutrity', 2, 11, 45, 12, 0),
          ('Russel', 'Liberry', 3, 13, 0, 14, 15),
          ('Natalya', 'Afforage', 2, 8, 15, 10, 0),
          ('Natalya', 'Nutrity', 4, 10, 10, 11, 45),
          ('Chihiro', 'Foodigm', 2, 9, 15, 9, 30),
          ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
          ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]

index = 'Chihiro'
d = (4, 12, 0)
output = []
final = []
output = backward_contact_trace(visits, index, d, 3)
[final.append(x) for x in output if x not in final]
final.sort()

print(final)

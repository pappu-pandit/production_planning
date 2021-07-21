def second_scored_std(listt):
    list_len = len(listt)
    dit = {}
    lit=[]
    for i in range(list_len):
        dit[listt[i][0]] = listt[i][1]
    all_values = set(dit.values())
    all_values.sort()
    for key, values in dit.items():
        if values == all_values[1]:
            lit.append(key)
        lit.sort()
    return lit



if __name__ == '__main__':
    listt = []
    for i in range(int(input())):
        listt.append([])
        for i in range(i, i + 1):
            name = str(input())
            score = float(input())
            listt[i].append(name)
            listt[i].append(score)

    ot=second_scored_std(listt)
    for i in range(len(ot)):
        print(ot[i])

def pizzareader(filename):

    slice = []

    with open(filename) as file:
        data = file.readlines()
        for line in data:
            word = line.rstrip("\n").split(" ")
            for element in word:
                slice.append(element)
        return slice
    file.close()


filename = "e_also_big.in"
le = pizzareader(filename)


def mainLogic(loote):

    maximum = int(loote[0])
    selected = []

    for pizza in range(len(loote) - 1, 1, -1):

        new_loote = int(loote[pizza])
        if new_loote < maximum:
            selected.append(pizza - 2)
            maximum = maximum - new_loote
        elif new_loote == maximum:
            selected.append(pizza - 2)
            break

    types = len(selected)
    selected.sort()

    with open(file_name, "w") as f:
        f.write("{}\n".format(types))
        for sol in selected:
            f.write("{} ".format(sol))


file_name = "e_sol.txt"


mainLogic(le)


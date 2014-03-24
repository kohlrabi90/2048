from random import randrange

def initialize():
    """ 4x4 Matrix initialisieren """
    liste = [[0 for i in range(4)] for j in range(4)]
    liste[0][1] = 2
    liste[2][2] = 2
    return liste


def print_list(field):
    """  Ausgabe der Matrix """
    for i in range(4):
        print("| ", end="")
        for j in range(4):
            print(field[i][j], end=" | ")
        print("")


def move(field, direction):
    if direction == 0:
        for y in range(4):
            x = 0
            while x < 4:
                while field[x][y] == 0:
                    field = shift(field, direction, x, y)
                if field[x][y] == -1:
                    field[x][y] = 0
                elif x > 0 and field[x][y] == field[x-1][y]:
                    field[x-1][y] *= 2
                    field = shift(field, direction, x, y)

                    while field[x][y] == 0:
                        field = shift(field, direction, x, y)
                    if field[x][y] == -1:
                        field[x][y] = 0

                x += 1
    elif direction == 1:
        for x in range(4):
            y = 3
            while y >= 0:
                while field[x][y] == 0:
                    field = shift(field, direction, x, y)
                if field[x][y] == -1:
                    field[x][y] = 0

                elif y < 3 and field[x][y] == field[x][y+1]:
                    field[x][y+1] *= 2
                    field = shift(field, direction, x, y)

                    while field[x][y] == 0:
                        field = shift(field, direction, x, y)
                    if field[x][y] == -1:
                        field[x][y] = 0

                y -= 1
    elif direction == 2:
        for y in range(4):
            x = 3
            while x >= 0:
                while field[x][y] == 0:
                    field = shift(field, direction, x, y)
                if field[x][y] == -1:
                    field[x][y] = 0

                elif x < 3 and field[x][y] == field[x+1][y]:
                    field[x+1][y] *= 2
                    field = shift(field, direction, x, y)

                    while field[x][y] == 0:
                        field = shift(field, direction, x, y)
                    if field[x][y] == -1:
                        field[x][y] = 0

                x -= 1
    elif direction == 3:
        for x in range(4):
            y = 0
            while y < 4:
                while field[x][y] == 0:
                    field = shift(field, direction, x, y)
                if field[x][y] == -1:
                    field[x][y] = 0

                elif y > 0 and field[x][y] == field[x][y-1]:
                    field[x][y-1] *= 2
                    field = shift(field, direction, x, y)

                    while field[x][y] == 0:
                        field = shift(field, direction, x, y)
                    if field[x][y] == -1:
                        field[x][y] = 0

                y += 1

    return random(field)


def shift(field, direction, x, y):
    if direction == 3:
        for i in range(y, 3):
            field[x][i] = field[x][i+1]

        field[x][3] = -1
    elif direction == 0:
        for i in range(x, 3):
            field[i][y] = field[i+1][y]

        field[3][y] = -1
    elif direction == 1:
        for i in range(y, 0, -1):
            field[x][i] = field[x][i-1]

        field[x][0] = -1
    elif direction == 2:
        for i in range(x, 0, -1):
            field[i][y] = field[i-1][y]

        field[0][y] = -1
    return field


def main():
    field = initialize()
    print_list(field)
    while 1:
        direction = input("direction (wasd): ")
        if direction == "w":
            field = move(field, 0)
        elif direction == "a":
            field = move(field, 3)
        elif direction == "s":
            field = move(field, 2)
        elif direction == "d":
            field = move(field, 1)
        else:
            print("Wrong input! Please enter wasd!")
            continue

        print_list(field)

def random(field):
    x = randrange(4)
    y = randrange(0, 3)
    while field[x][y] != 0:
        x = randrange(4)
        y = randrange(4)

    if randrange(10) > 1:
        field[x][y] = 2
    else:
        field[x][y] = 4

    return field

if __name__ == "__main__":
    main()
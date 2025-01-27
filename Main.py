import random

POSSIBLE_SEAT_STATES = ['A', 'S', 'K', 'E']

def InitSeats(seats: list) -> None:
    for i in range(15):
        seats.append([[], []])

    return seats

def FillUpSeats(seats: list) -> None:
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            for k in range(10):
                seats[i][j].append(POSSIBLE_SEAT_STATES[random.randint(0, 3)])

    return seats

def RequestSeats(seatAmount: int, seats: list) -> int:
    availableNumSeatsInRow: int = 0

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            for k in range(len(seats[i][j])):
                if seats[i][j][k] == 'E':
                    availableNumSeatsInRow += 1
                else:
                    availableNumSeatsInRow = 0

                if availableNumSeatsInRow == seatAmount:
                    return i + 1

    return -1

def PrintSeats(seats: list) -> None:
    for i in range(len(seats)):
        print(seats[i])

def CalcIncome(seats: list) -> int:
    income: int = 0

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            for k in range(len(seats[i][j])):
                if seats[i][j][k] == 'A':
                    income += 2500
                elif seats[i][j][k] == 'S':
                    income += 2100
                elif seats[i][j][k] == 'E':
                    income += 1300

    return income

def SeatUtilization(seats: list) -> float:
    usedSeatsCont: int = 0

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            for k in range(len(seats[i][j])):
                if seats[i][j][k] != 'E':
                    usedSeatsCont += 1

    utilization: float = usedSeatsCont / (15 * 20)
    return utilization

def CountFullPricePass(seats: list) -> int:
    fullPricePassCount: int = 0

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            for k in range(len(seats[i][j])):
                if seats[i][j][k] == 'A':
                    fullPricePassCount += 1

    return fullPricePassCount

def Main() -> None:
    seats: list = []
    InitSeats(seats)
    FillUpSeats(seats)

    howManySeatsNeeded = -1
    print("Mennyi ülőhelyet kíván az emberünk: ", end='')
    try:
        howManySeatsNeeded = int(input())
    except:
        print("Kérem számot adjon meg!")

    while howManySeatsNeeded not in range(2, 6):
        print("Kérem 2 és 5 között adjon értéket: ", end='')
        try:
            howManySeatsNeeded = int(input())
        except:
            print("Kérem számot adjon meg!")

    reqSeatRes = RequestSeats(howManySeatsNeeded, seats)
    if reqSeatRes < 0:
        print("Nincsen annyi üres szék egymás mellet amennyit kért")
    else:
        print(f"A {reqSeatRes}. sorban vannak a székeik")

    print(f"Mozi bevétel: {CalcIncome(seats)}Ft")
    print(f"Terem felhasználtsága: {round(SeatUtilization(seats) * 100, 2)}%")
    print(f"Teljes árú jegyek száma: {CountFullPricePass(seats)}db")

if __name__ == "__main__":
    Main()
